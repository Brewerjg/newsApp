from django.shortcuts import render
import requests

def index(request):
    # Code from index function
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=d4c18b0cb8854efbbbdcf18221e930fc')
    res = r.json()
    data = res.get("articles")
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

    # Code from tech function
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=d4c18b0cb8854efbbbdcf18221e930fc')
    res = r.json()
    data = res.get("articles")
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
    techNews = zip(title, description, urlToImage, url)

    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d4c18b0cb8854efbbbdcf18221e930fc')
    res = r.json()
    data = res.get("articles")
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
    busNews = zip(title, description, urlToImage, url)
    
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=d4c18b0cb8854efbbbdcf18221e930fc')
    res = r.json()
    data = res.get("articles")
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
    sciNews = zip(title, description, urlToImage, url)
    
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=d4c18b0cb8854efbbbdcf18221e930fc')
    res = r.json()
    data = res.get("articles")
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
    entNews = zip(title, description, urlToImage, url)
    
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=d4c18b0cb8854efbbbdcf18221e930fc')
    res = r.json()
    data = res.get("articles")
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
    sportNews = zip(title, description, urlToImage, url)

    return render(request, 'newsApplication/index.html', context={'news': news, 'techNews': techNews, 'busNews': busNews, 'sciNews': sciNews, 'entNews': entNews, 'sportNews': sportNews})
