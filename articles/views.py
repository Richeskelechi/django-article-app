from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .import forms

# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articleList.html', {'articles': articles})


def each_list(request, param):
    # return HttpResponse(param)
    each_article = Article.objects.get(slug=param)
    return render(request, 'articles/eachArticle.html', {'article': each_article})


@login_required(login_url='/accounts/signin/')
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # we are storing the form in a variable called instance
            instance = form.save(commit=False)
            # now we are adding the author which is the logged in user to the instance of the form
            instance.author = request.user
            # now we are doing the actual saving to DB
            instance.save()
            return redirect('articles:article_list')
            # return render(request, 'articles/eachArticle.html', {'article': form.cleaned_data})
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
