from django.shortcuts import render
import random
from .models import Article

# Create your views here.
def catch(request):
    context = {
        'message': request.GET.get('message'),
    }

    return render(request, 'articles/catch.html', context)

def detail(request, num):
    context = {
        'num': num,
    }

    return render(request, 'articles/detail.html', context)

def dinner(request):
    foods = [
        '국밥',
        '국수',
        '카레',
        '탕수육',
    ]
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }

    return render(request, 'articles/dinner.html', context)

def greeting(request):
    pass

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')