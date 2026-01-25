import requests #get the contest of the webpage

apiKey="c3daa79d998c426490672da8c02bdf05"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=c3daa79d998c426490672da8c02bdf05"

#get the contest
request = requests.get(url)
content = request.text
#print(content)