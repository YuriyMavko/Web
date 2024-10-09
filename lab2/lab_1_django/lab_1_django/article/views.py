from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        article = Article.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'articles/create.html')

def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('index')