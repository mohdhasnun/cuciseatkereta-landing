from html.parser import HTMLParser
from collections import Counter
from pathlib import Path
import re,subprocess,json
BASE='1d0348e'
old=subprocess.check_output(['git','show',BASE+':index.html']).decode()
new=Path('index.html').read_text(encoding='utf-8')
class Content(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.skip=0;self.words=[];self.ids=[];self.links=[];self.headings=[];self.h=None;self.parts=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ('script','style'):self.skip+=1
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a' and a.get('href'):self.links.append(a['href'])
  if tag in ('h1','h2','h3'):self.h=tag;self.parts=[]
  if tag=='br' and self.h:self.parts.append(' ')
 def handle_endtag(self,tag):
  if tag in ('script','style'):self.skip-=1
  if tag==self.h:self.headings.append((tag,' '.join(''.join(self.parts).split())));self.h=None
 def handle_data(self,text):
  if self.skip:return
  t=' '.join(text.split())
  if t:self.words.append(t)
  if self.h:self.parts.append(text)
a=Content();a.feed(old);b=Content();b.feed(new)
missing=list((Counter(a.words)-Counter(b.words)).elements())
missing_headings=list((Counter(a.headings)-Counter(b.headings)).elements())
missing_links=list((Counter(a.links)-Counter(b.links)).elements())
schema=lambda x:re.findall(r'<script type="application/ld\+json">(.*?)</script>',x,re.S)
conv=lambda x:x.split('<!-- WHATSAPP_CONVERSION_START -->')[1].split('<!-- WHATSAPP_CONVERSION_END -->')[0]
checks={'all_original_text_preserved':not missing,'all_original_headings_preserved':not missing_headings,'all_original_links_preserved':not missing_links,'original_ids_preserved':not(set(a.ids)-set(b.ids)),'unique_ids':len(b.ids)==len(set(b.ids)),'metadata_unchanged':old[:old.index('<style>')]==new[:new.index('<style>')],'schema_unchanged':schema(old)==schema(new),'conversion_unchanged':conv(old)==conv(new),'three_customer_cases':new.count('class="customer-case"')==3,'eight_faq_questions':new.count('class="faq-card"')==8,'four_primary_service_cards':new.count('class="price-service"')==4}
report={'baseline':BASE,'checks':checks,'missing_text':missing,'missing_headings':missing_headings,'missing_links':missing_links}
print(json.dumps(report,ensure_ascii=False,indent=2))
Path('../../outputs/redesign-content-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
assert all(checks.values())
