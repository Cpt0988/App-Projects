import requests #get the contest of the webpage
from send_email import send_email


apiKey="c3daa79d998c426490672da8c02bdf05"
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-05-24&sortBy=publishedAt&apiKey=c3daa79d998c426490672da8c02bdf05"

#make a request, get dictionary with data & access article title and description
request = requests.get(url)
content = request.json()
body =""
for article in content["articles"]:
    if article["title"]is not None:
        body = body + article["title"] + "\n"+ article["description"] + 2*"\n"
body=body.encode("utf-8")   
send_email(message=body)
    
    