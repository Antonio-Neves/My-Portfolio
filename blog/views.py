from django.views.generic import DetailView
from base.views import ContactFormView

from blog.models import Article


# --- Articles --- #
class ArticleDetailView(DetailView, ContactFormView):
	model = Article
	slug_field = 'article_slug'
	template_name = 'blog/article-detail.html'
