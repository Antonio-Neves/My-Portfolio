from django.shortcuts import render
from django.http import FileResponse
from my_portfolio.settings import BASE_DIR
from django.views.generic import TemplateView


# --- Home Page --- #
class IndexView(TemplateView):
	template_name = 'principal/index.html'


def download_cv(request):
	file_path = BASE_DIR / 'files/Cv_Antonio_Neves_2021.pdf'

	response = FileResponse(open(file_path, 'rb'))

	return response
