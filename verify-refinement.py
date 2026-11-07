"""Regression checks for the explicitly approved content consolidation."""
from html.parser import HTMLParser
from pathlib import Path
import re,subprocess,json
from urllib.parse import urlparse,parse_qs
old=subprocess.check_output(['git','show','a91278d:index.html']).decode()
new=Path('index.html').read_text(encoding='utf-8')
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.anchors=[];self.wa=[];self.media=[];self.skip=0;self.text=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t in ('script','style'):self.skip+=1
  if a.get('id'):self.ids.append(a['id'])
  if t=='a' and a.get('href','').startswith('#'):self.anchors.append(a['href'][1:])
  if t=='a' and a.get('href','').startswith('https://wa.me/'):self.wa.append(a)
  if a.get('src','').startswith('assets/'):self.media.append(a['src'].split('?')[0])
 def handle_endtag(self,t):
  if t in ('script','style'):self.skip-=1
 def handle_data(self,s):
  if not self.skip:self.text.extend(s.split())
a=Page();a.feed(old);b=Page();b.feed(new)
def parts(s,pattern):return re.findall(pattern,s,re.S)
def h1(s):return ' '.join(re.sub('<[^>]+>',' ',parts(s,r'<h1\b[^>]*>(.*?)</h1>')[0]).split())
def conv(s):return s.split('<!-- WHATSAPP_CONVERSION_START -->')[1].split('<!-- WHATSAPP_CONVERSION_END -->')[0]
checks={
 'metadata_canonical_unchanged':old[:old.index('<style>')]==new[:new.index('<style>')],
 'schema_unchanged':parts(old,r'<script type="application/ld\+json">(.*?)</script>')==parts(new,r'<script type="application/ld\+json">(.*?)</script>'),
 'conversion_code_unchanged':conv(old)==conv(new),
 'one_h1_same_headline':len(parts(new,r'<h1\b'))==1 and h1(old)==h1(new),
 'three_cases_unchanged':len(parts(new,r'<article class="customer-case".*?</article>'))==3 and parts(old,r'<article class="customer-case".*?</article>')==parts(new,r'<article class="customer-case".*?</article>'),
 'four_service_cards_unchanged':len(parts(new,r'<article class="price-service".*?</article>'))==4 and parts(old,r'<article class="price-service".*?</article>')==parts(new,r'<article class="price-service".*?</article>'),
 'eight_faq_answers_unchanged':len(parts(new,r'<details class="faq-card">.*?</details>'))==8 and parts(old,r'<details class="faq-card">.*?</details>')==parts(new,r'<details class="faq-card">.*?</details>'),
 'reviews_match_verified_sources':all(t in new for t in ('Was very careful with my 38 yo car seat.', 'Boss is very friendly, professional, and efficient.', 'Bau hilang, seat nampak macam baru, dan servis sangat teliti. Saya datang dari Putrajaya, memang berbaloi.', 'Rupert Chen', 'Weng Ji', 'Fatin Syafinaz', 'Petikan ulasan Google')) and new.count('class="testi-text"')==3,
 'service_price_ranges_unchanged':parts(old,r'<span class="service-price">.*?</span>')==parts(new,r'<span class="service-price">.*?</span>'),
 'address_hours_unchanged':parts(old,r'<p class="shop-details">.*?</p>')==parts(new,r'<p class="shop-details">.*?</p>') and 'D-00-01, Pangsapuri Mawar Jaya, Jalan KP 4/4, Taman Kota Perdana, 43300 Seri Kembangan, Selangor.' in new,
 'all_original_ids_retained':not(set(a.ids)-set(b.ids)),
 'no_duplicate_ids':len(b.ids)==len(set(b.ids)),
 'all_fragment_links_resolve':not(set(b.anchors)-set(b.ids)),
 'all_whatsapp_ctas_valid':len(b.wa)>0 and all(urlparse(x['href']).path=='/60176993876' and parse_qs(urlparse(x['href']).query).get('text') and x.get('target')=='_blank' and 'noopener' in x.get('rel','') for x in b.wa),
 'all_local_media_exist':all(Path(x).is_file() for x in b.media),
 'booking_route_unchanged':Path('book/index.html').read_text(encoding='utf-8')==subprocess.check_output(['git','show','a91278d:book/index.html']).decode(),
 'three_advantages':len(parts(parts(new,r'<div class="refinement-advantages">(.*?)</div>')[0],r'<article>'))==3,
 'three_gallery_comparison_sliders':new.count('class="case-media case-compare gallery-compare"')==3,
 'duplicate_case_footer_removed':'class="cases-footer"' not in new,
 'redundant_panels_removed':all(x not in new for x in ('class="service-overview"','class="about"','class="mid-cta"','class="problems"','booking-detail','Butiran servis, skop cucian &amp; tentang kedai kami')),
 'lighter_text_content':len(b.text)<len(a.text)
}
report={'baseline':'a91278d','checks':checks,'original_words':len(a.text),'refined_words':len(b.text),'whatsapp_ctas_checked':len(b.wa),'missing_ids':sorted(set(a.ids)-set(b.ids)),'broken_fragments':sorted(set(b.anchors)-set(b.ids))}
print(json.dumps(report,ensure_ascii=False,indent=2))
Path('../../outputs/refinement-content-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
assert all(checks.values())
