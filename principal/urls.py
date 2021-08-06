from django.urls import path

from principal.views import index

urlpatterns = [
	path('', index, name='index')
]
