from django.shortcuts import render
from .models import Article


def beautiful_slovenia(request):
    articles = Article.objects.filter(status_article="active")
    context = {"articles": articles}
    return render(request, 'beautiful_slovenia/index.html', context=context)
