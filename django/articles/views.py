from django.shortcuts import render, redirect
import random
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def catch(request):
    context = {
        'message': request.GET.get('message'),
    }

    return render(request, 'articles/catch.html', context)

@login_required
def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # # 유효성 검사를 위해 데이터 정비와 저장을 분리
    # article = Article(title=title, content=content)
    # article.save()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # 저장된 객체를 반환
            article = form.save()
            
            # 저장 후, 페이지 응답은 POST 요청에 대한 적절한 응답은 아님
            # >> 기술 : POST 요청은 데이터 생성/변경에 사용되며 동일 요청이 반복되면 안됨
            # >> UX : 후속 행동 유발로 예기치 않은 동작 발생 가능
            # Redirect : 서버가 클라이언트를 직접 다른 페이지로 보내는 것이 아닌 클라이언트가 GET 요청을 다시하도록 유도
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    
    # - 유효성 검사를 통과하지 못한 경우, 해당 페이지를 에러 메세지와 함께 다시 응답
    # - 데이터 생성을 위한 GET 요청의 경우
    context = {
        'form': form,
    }
    
    return render(request, 'articles/create.html', context)

    
    

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    
    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

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

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)

#     form = ArticleForm(instance=article)


#     context = {
#         'article': article,
#         'form': form,
#     }

#     return render(request, 'articles/edit.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    
    # article.title = title
    # article.content = content
    # article.save()

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()

            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }

    return render(request, 'articles/update.html', context)

def greeting(request):
    pass

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

# def new(request):
#     form = ArticleForm()

#     context = {
#         'form': form,
#     }

#     return render(request, 'articles/new.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')