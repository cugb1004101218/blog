from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from article.models import Article, Category

# Create your views here.
def index(request):
    return HttpResponse("这是首页")

class HomeView(TemplateView):
    template_name = 'home/home.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        all_category = Category.objects.all()
        context["all_category"] = all_category
        return context
