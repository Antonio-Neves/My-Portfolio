from django.urls import path

from principal.views import download_cv, IndexView

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('download-cv/', download_cv, name='download-cv')
]
