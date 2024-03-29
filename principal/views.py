from django.shortcuts import render
from django.http import FileResponse
from my_portfolio.settings import BASE_DIR
from django.views.generic import TemplateView

from base.views import ContactFormView


# --- Home Page --- #
class IndexView(TemplateView, ContactFormView):
	template_name = 'principal/index.html'


# --- Download CV --- #
def download_cv(request):
	file_path = BASE_DIR / 'files/CV_Antonio_Neves_2024.pdf'

	response = FileResponse(open(file_path, 'rb'))

	return response
