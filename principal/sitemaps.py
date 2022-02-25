# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from blog.models import Article


class BlogPostSitemap(Sitemap):
	changefreq = "weekly"

	def items(self):
		return Article.objects.all()

	def lastmod(self, obj):
		return obj.modified_at


class StaticViewSitemap(Sitemap):
	changefreq = 'monthly'

	def items(self):
		return ['index']

	def location(self, item):
		return reverse(item)