from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.views.generic import TemplateView, DetailView

from principal.forms import ContactForm
from blog.models import Category, SubCategory, Article


# --- Articles --- #
class ArticleDetailView(DetailView, FormView):
	model = Article
	slug_field = 'article_slug'
	template_name = 'blog/article-detail.html'
	form_class = ContactForm
	success_url = reverse_lazy('index')

	def form_valid(self, form, *args, **kwargs):
		form.send_mail()
		return super(ArticleDetailView, self).form_valid(form)

	def form_invalid(self, form, *args, **kwargs):
		return super(ArticleDetailView, self).form_invalid(form)
