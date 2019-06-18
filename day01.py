import requests
# 请求百度，需要注意：一定带上http/https
response = requests.get('http://www.baidu.com')
print(response)
print(response.headers)

