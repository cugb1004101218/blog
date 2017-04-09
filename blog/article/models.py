from django.db import models

# Create your models here.
class Category(models.Model):
    literal = models.CharField(max_length=200, blank=True)
    summary = models.TextField()
    def __str__(self):
        return self.literal

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    visit_num = models.IntegerField()
    content = models.TextField()
    title = models.CharField(max_length=200)
    publish_time = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")
    category = models.ForeignKey(Category, blank=True, null=True, related_name="category_article")
    index = models.IntegerField()
    video_url = models.CharField(max_length=2000, blank=True)
    def __str__(self):
        return self.title
