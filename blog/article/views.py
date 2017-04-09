from django.shortcuts import render
from django.views.generic import TemplateView

from article.models import Article, Category

# Create your views here.
class ArticleDetailView(TemplateView):
    model = Article
    template_name = 'article/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        category_literal = self.request.GET.get('category', None)
        article_list = Article.objects.all().filter(is_published=True).order_by("index")
        if category_literal:
          category = Category.objects.get(literal=category_literal)
          context["now_category"] = category
          article_list = article_list.filter(category=category)
        context["article_list"] = article_list
        article_id = self.request.GET.get('article_id')
        article = None
        if not article_id:
            if len(article_list) > 0:
              article = article_list[0]
        else:
            article = Article.objects.get(article_id=article_id, is_published=True)
        context["article"] = article
        article_pos = -1
        for i in range(0, len(article_list)):
            if article.article_id == article_list[i].article_id:
                article_pos = i
        if article_pos == -1:
            context["next_article_id"] = "#"
            context["pre_article_id"] = "#"
        else:
            context["pre_article_id"] = article_list[max(article_pos - 1, 0)].article_id
            context["next_article_id"] = article_list[min(article_pos + 1, len(article_list) - 1)].article_id
        all_category = Category.objects.all()
        context["all_category"] = all_category
        print (context)
        return context
