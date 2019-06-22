import requests
url = '"graph.baidu.com": "http://graph.baidu.com"'
res = url.split(':')[-1]
print(res)
with open(res,'w',encoding='utf8') as f:
    f.write(res.text)