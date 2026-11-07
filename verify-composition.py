"""Content/behaviour regression gates for the final composition refinement."""
from html.parser import HTMLParser
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse,parse_qs
import re,subprocess,json
BASE='df9f3da'
old=subprocess.check_output(['git','show',BASE+':index.html']).decode()
new=Path('index.html').read_text(encoding='utf-8')
class Document(HTMLParser):
 def __init__(self,s):
  super().__init__(convert_charrefs=False);self.s=s;self.nodes=[];self.stack=[];self.lines=[0]
  for line in s.splitlines(keepends=True):self.lines.append(self.lines[-1]+len(line))
  self.feed(s)
 def pos(self):
  a,b=self.getpos();return self.lines[a-1]+b
 def handle_starttag(self,t,attrs):
  node={'tag':t,'attrs':dict(attrs),'start':self.pos(),'end':self.pos()+len(self.get_starttag_text())};self.nodes.append(node)
  if t not in ('area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'):self.stack.append(node)
 def handle_startendtag(self,t,attrs):self.nodes.append({'tag':t,'attrs':dict(attrs),'start':self.pos(),'end':self.pos()+len(self.get_starttag_text())})
 def handle_endtag(self,t):
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i]['tag']==t:self.stack[i]['end']=self.pos()+len('</'+t+'>');del self.stack[i:];break
 def all(self,t=None,ident=None,cls=None):
  return [n for n in self.nodes if (not t or n['tag']==t) and (not ident or n['attrs'].get('id')==ident) and (not cls or cls in n['attrs'].get('class','').split())]
 def raw(self,n):return self.s[n['start']:n['end']]
 def get(self,t=None,ident=None,cls=None):return self.raw(self.all(t,ident,cls)[0])
 def ids(self):return [n['attrs']['id'] for n in self.nodes if 'id' in n['attrs']]
 def wa(self):return [n['attrs'] for n in self.all('a') if n['attrs'].get('href','').startswith('https://wa.me/')]
a=Document(old);b=Document(new)
def parts(s,p):return re.findall(p,s,re.S)
def conv(s):return s.split('<!-- WHATSAPP_CONVERSION_START -->')[1].split('<!-- WHATSAPP_CONVERSION_END -->')[0]
def first_p_by_question(d):
 return {re.sub('<[^>]+>','',parts(d.raw(n),r'<summary>(.*?)</summary>')[0]):parts(d.raw(n),r'<p\b[^>]*>.*?</p>')[0] for n in d.all('details',cls='faq-card')}
faq_before=first_p_by_question(a);faq_after=first_p_by_question(b)
full_before=Document(a.get('article',ident='servis-pakej-dalaman'));full_after=Document(b.get('article',ident='servis-pakej-dalaman'))
extra=Document(b.get('details',cls='other-prices'))
ids=b.ids();broken=[n['attrs']['href'] for n in b.all('a') if n['attrs'].get('href','').startswith('#') and n['attrs']['href'][1:] not in ids]
media_before=[n['attrs'] for n in Document(a.get('section',ident='hasil')).all('img')]
media_after=[n['attrs'] for n in Document(b.get('section',ident='hasil')).all('img')]
expected_advantages=['Kenal pasti masalah','Cucian mengikut keadaan','Harga jelas sebelum kerja']
advantages=parts(b.get('div',cls='refinement-advantages'),r'<h3>(.*?)</h3>')
checks={
 'metadata_canonical_unchanged':old[:old.index('<style>')]==new[:new.index('<style>')],
 'structured_data_unchanged':parts(old,r'<script type="application/ld\+json">(.*?)</script>')==parts(new,r'<script type="application/ld\+json">(.*?)</script>'),
 'conversion_code_unchanged':conv(old)==conv(new),
 'approved_hero_html_unchanged':a.get('section',cls='hero')==b.get('section',cls='hero'),
 'approved_header_html_unchanged':a.get('header',cls='site-header')==b.get('header',cls='site-header'),
 'one_h1':len(b.all('h1'))==1,
 'all_whatsapp_links_messages_preserved':Counter(x['href'] for x in a.wa())==Counter(x['href'] for x in b.wa()),
 'whatsapp_destinations_valid':all(urlparse(x['href']).path=='/60176993876' and parse_qs(urlparse(x['href']).query).get('text') and x.get('target')=='_blank' and 'noopener' in x.get('rel','') for x in b.wa()),
 'booking_route_unchanged':Path('book/index.html').read_text(encoding='utf-8')==subprocess.check_output(['git','show',BASE+':book/index.html']).decode(),
 'primary_prices_unchanged':parts(old,r'<div class="price-service-value">(.*?)</div>')==parts(new,r'<div class="price-service-value">(.*?)</div>'),
 'full_interior_scope_rm600_unchanged':full_before.get('p',cls='service-description')==full_after.get('p',cls='service-description') and '>RM600<' in b.get('article',ident='servis-pakej-dalaman'),
 'additional_price_ranges_unchanged':parts(old,r'<span class="service-price">(.*?)</span>')==parts(new,r'<span class="service-price">(.*?)</span>'),
 'additional_price_rows_only':len(extra.all('article'))==3 and not extra.all('p'),
 'all_eight_faqs_and_original_answers_preserved':len(faq_after)==8 and faq_before==faq_after,
 'verified_testimonials_unchanged':parts(old,r'<p class="testi-text">.*?</p>')==parts(new,r'<p class="testi-text">.*?</p>'),
 'gallery_photos_alt_and_sizes_unchanged':media_before==media_after,
 'five_comparison_sliders':len(b.all('input'))==len(a.all('input')) and len(b.all('div',cls='case-compare'))==5,
 'three_real_cases':len(b.all('article',cls='customer-case'))==3,
 'case_media_unchanged':all(Document(a.get('article',ident=ident)).get('div',cls='case-media')==Document(b.get('article',ident=ident)).get('div',cls='case-media') for ident in ['kes-bau-muntah','kes-air-kencing','kes-air-hujan']),
 'urine_result_not_overclaimed':'Hasil rawatan bau belum disahkan.' in b.get('article',ident='kes-air-kencing'),
 'video_poster_preload_and_no_autoplay':a.get('video')==b.get('video') and 'preload="none"' in b.get('video') and 'autoplay' not in b.get('video'),
 'three_requested_advantages':advantages==expected_advantages,
 'gallery_requested_title':'Hasil Cucian Sebenar.' in b.get('section',ident='hasil'),
 'reviews_and_visit_sections_separate':bool(b.all('section',ident='ulasan')) and bool(b.all('section',cls='assurance-location')) and not b.all('div',cls='trust-hub'),
 'all_original_ids_retained':not(set(a.ids())-set(ids)),
 'no_duplicate_ids':len(ids)==len(set(ids)),
 'all_anchor_links_resolve':not broken,
 'hours_and_shop_only_status_preserved':a.get('p',cls='shop-details')==b.get('p',cls='shop-details'),
 'full_address_preserved':'D-00-01, Pangsapuri Mawar Jaya, Jalan KP 4/4, Taman Kota Perdana, 43300 Seri Kembangan, Selangor.' in new,
 'local_media_exist':all(Path(n['attrs']['src'].split('?')[0]).is_file() for n in b.nodes if n['attrs'].get('src','').startswith('assets/')),
 'unverified_payment_strip_removed':not b.all('div',cls='pay-strip-wrap'),
}
report={'baseline':BASE,'checks':checks,'whatsapp_ctas_checked':len(b.wa()),'missing_ids':sorted(set(a.ids())-set(ids)),'broken_anchors':broken}
print(json.dumps(report,ensure_ascii=False,indent=2))
Path('../../outputs/final-composition-content-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
assert all(checks.values())
