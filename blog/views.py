from django.http import Http404

from django.views.generic import DetailView, ListView
from base.views import ContactFormView

from blog.models import Article


# --- Blog Home --- #
class BlogHomeView(ListView, ContactFormView):
	model = Article
	template_name = 'blog/blog.html'


# --- Articles --- #
class ArticleDetailView(DetailView, ContactFormView):
	model = Article
	slug_field = 'article_slug'
	template_name = 'blog/article-detail.html'

	def get(self, request, *args, **kwargs):
		"""
		Changed Get method because if article is not published
		return page not found
		"""

		self.object = self.get_object()
		context = self.get_context_data(object=self.object)

		if self.object.article_status == '1':
			return self.render_to_response(context)
		else:
			raise Http404