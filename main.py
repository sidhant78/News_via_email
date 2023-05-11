import requests
from send_email import gmailer
api_key = "808afafda5b549b5a3e6fe62b8e381f4"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-04-11&sortBy=publishedAt&apiKey=" \
      "808afafda5b549b5a3e6fe62b8e381f4"
request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"]:
    body = body + article['title'] + "\n" + article['description'] + 2*'\n'
body = body.encode('utf-8')
gmailer(body)

