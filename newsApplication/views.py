from django.shortcuts import render
import requests

def index(request):
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=d4c18b0cb8854efbbbdcf18221e930fc')
    res = r.json()
    data = res.get("articles")  # Fix error with data = ["data"]
    title = []
    description = []
    urlToImage = []
    url = []
    for i in range(len(data)):
        f = data[i]
        title.append(f['title'])
        description.append(f['description'])
        urlToImage.append(f['urlToImage'])
        url.append(f['url'])
    news = zip(title, description, urlToImage, url)
    return render(request, 'newsApplication/index.html', context={'news': news})
