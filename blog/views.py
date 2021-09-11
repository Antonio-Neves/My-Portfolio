from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from blog.models import Category, SubCategory, Article


# --- Articles --- #
class ArticleDetailView(DetailView):
	model = Article
	slug_field = 'article_slug'
	template_name = 'blog/article-detail.html'
	# context_object_name = 'article'