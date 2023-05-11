import requests
from send_email import gmailer
topic = "tesla"
api_key = "808afafda5b549b5a3e6fe62b8e381f4"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-04-11&" \
      "sortBy=publishedAt&" \
      "apiKey=" \
      "808afafda5b549b5a3e6fe62b8e381f4&" \
      "language=en"
request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"][:15]:
    body ="news of the day:" + "\n" + body + article['title'] + "\n" + article['description'] + "\n" + article['url'] + 2*'\n'
body = body.encode('utf-8')
gmailer(body)

