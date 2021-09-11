from django.urls import path

from blog.views import (
	ArticleDetailView,
)

urlpatterns = [
	path('article/<slug:slug>/',
		 ArticleDetailView.as_view(), name='article-detail'),
]
