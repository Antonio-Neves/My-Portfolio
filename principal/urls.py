from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogPostSitemap, StaticViewSitemap

from principal.views import download_cv, IndexView

sitemaps = {
    'posts': BlogPostSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('download-cv/', download_cv, name='download-cv'),
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
