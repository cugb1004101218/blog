from django.conf.urls import url

from article.views import ArticleDetailView

urlpatterns = [
    url(r'^$', ArticleDetailView.as_view(), name='article_detail'),
]
