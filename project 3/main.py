import requests #get the contest of the webpage

apiKey="c3daa79d998c426490672da8c02bdf05"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=c3daa79d998c426490672da8c02bdf05"

#make a request, get dictionary with data & access article
request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])