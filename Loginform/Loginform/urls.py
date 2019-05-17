"""Loginform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    ИЛИ url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from django.urls import path #не работает выдает ошибку не правильный синтаксис
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from django.conf.urls import url
# или импорт url а не path
# url(r'^$', views.home, name='home')
# from . точка значит импортируем из этой же дирректории

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^articles/',include('articles.urls')), # делаем import include и далее берет в articles потом urls
    url(r'^about/$',views.about), # views файл который импортнули .about функция которая во views. # если вызван url about то вызываем функции
    url(r'^$',views.homepage), # homepage. ^ - это старт. $ - это конец. ничего по середине нету. для того что бы перейти на название сайта .ee и все
    # затем делаем файо views.py и там создаем функции для about
]

urlpatterns += staticfiles_urlpatterns()