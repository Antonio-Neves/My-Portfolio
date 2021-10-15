from django.urls import path

from blog.views import (
	BlogHomeView,
	ArticleDetailView
)

urlpatterns = [
	path('', BlogHomeView.as_view(), name='blog'),
	path('article/<slug:slug>/',
		 ArticleDetailView.as_view(), name='article-detail'),
]
