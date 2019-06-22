import requests
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
print(HTML)
if farm1 in HTML:
    url1.append(HTML)
elif farm2 in HTML:
    url2.append(HTML)
else:
    url3.append(HTML)