import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'wd':'娃哈哈'})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)


data = bytes(urllib.parse.urlencode({'pw':'595355490','acc':'741852963'}),enconding='utf8')
url = 'https://mail.163.com/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)