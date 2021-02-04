import requests
import re
import hashlib

url = 'http://134.122.108.157:32592/'
reqsesh = requests.session()

#get
get = reqsesh.get(url)
htmlout = get.text

def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

out = remove_html_tags(htmlout)
out1 = out.split(' string')[1].strip()
hashmd5 = hashlib.md5(out1.encode('utf-8')).hexdigest()

#post
postdata = dict(hash=hashmd5)
post = reqsesh.post(url=url, data=postdata)

print(post.text)
