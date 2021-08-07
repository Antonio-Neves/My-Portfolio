from django.shortcuts import render
from django.views.generic import TemplateView


# --- Home Page --- #
class IndexView(TemplateView):
	template_name = 'principal/index.html'
