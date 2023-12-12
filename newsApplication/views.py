from django.shortcuts import render
import requests

def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=741a516a62637aed5ab6a1e4d87e38cc&countries=au,-us')
    res = r.json()
    data = res.get("data")  # Fix error with data = ["data"]
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    news = zip(title, description, image, url)
    return render(request, 'newsApplication/index.html', {'news': news})
