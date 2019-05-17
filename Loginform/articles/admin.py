from django.contrib import admin
from .models import Article
# .models модель файлы в текущую директорию. ЗНАЧИТ С ТОЧКОЙ !!!!

admin.site.register(Article)