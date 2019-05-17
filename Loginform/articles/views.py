from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.
def article_list(request):
    articles=Article.objects.all().order_by('date') # by date новые будут первые
    return render(request,'articles/article_list.html',{'articles':articles}) #ставим словарь {}

def article_detail(request,slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

    