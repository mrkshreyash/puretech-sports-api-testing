import requests

url = "https://inshorts.deta.dev/news?category=sports"
response = requests.get(url=url)
print(response.content)
