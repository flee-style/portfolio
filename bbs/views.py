from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm, ArticleForm


# Create your views here.

def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        searchtext = searchForm.cleaned_data['searchtext']
        articles = Article.objects.filter(content__contains=searchtext)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
        'message': 'welcome bbs',
        'articles': articles,
        'searchForm': searchForm,
    }

    return render(request, 'bbs/index.html', context)


def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        'article': article,
    }

    return render(request, 'bbs/detail.html', context)


def new(request):
    # フォーム使用
    articleForm = ArticleForm()
    context = {
        'message': 'new bbs',
        'articleForm': articleForm,
    }
    return render(request, 'bbs/new.html', context)
    # createで保存されるかチェック


def create(request):
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            article = articleForm.save()
    context = {
        'message': 'Create article' + str(article.id),
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)


def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    articles = Article.objects.all()
    context = {
        'message': 'Delete article',
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context)


def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    articleForm = ArticleForm(instance=article)

    context = {
        'message': 'Edit Article',
        'article': article,
        'articleForm': articleForm,
    }

    return render(request, 'bbs/edit.html', context)

def update(request,id):
    if request.method == 'POST':
        article = get_object_or_404(Article,pk=id)
        articleForm = ArticleForm(request.POST,instance=article)
        if articleForm.is_valid():
            article = articleForm.save()
    context = {
        'message' : 'article' + str(article.id) +'updated',
        'article' : article
    }

    return render(request,"bbs/detail.html",context)