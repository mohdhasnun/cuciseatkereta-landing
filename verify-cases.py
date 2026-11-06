from pathlib import Path
import subprocess,re,json
s=Path('index.html').read_text(encoding='utf-8')
old=subprocess.check_output(['git','show','68f6df120768d2c9db8f44b0e7711b419528ea31:index.html']).decode()
head=lambda x:x[:x.index('<style>')]
conversion=lambda x:x.split('<!-- WHATSAPP_CONVERSION_START -->')[1].split('<!-- WHATSAPP_CONVERSION_END -->')[0]
checks={'metadata_and_schema_unchanged':head(s)==head(old),'conversion_unchanged':conversion(s)==conversion(old),'three_cases_in_html':s.count('class="customer-case"')==3}
for name,pattern in [('prices',r'<section class="catalog".*?</section>'),('reviews',r'<section class="testi".*?</section>'),('location',r'<section class="area".*?</section>')]:
    a=re.search(pattern,s,re.S); b=re.search(pattern,old,re.S)
    checks[name+'_unchanged']=bool(a and b and a.group()==b.group())
print(json.dumps(checks,indent=2))
assert all(checks.values())
