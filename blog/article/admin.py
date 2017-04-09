from django.contrib import admin
from article.models import Article, Category

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'title', 'content') #You can use 'pk' or 'id'
admin.site.register(Article, MyModelAdmin)
admin.site.register(Category)

