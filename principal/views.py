from django.shortcuts import render
from django.http import FileResponse
from my_portfolio.settings import BASE_DIR
from django.views.generic import FormView
from django.urls import reverse_lazy

from principal.forms import ContactForm


# --- Home Page --- #
class IndexView(FormView):
	template_name = 'principal/index.html'
	form_class = ContactForm
	success_url = reverse_lazy('index')

	def form_valid(self, form, *args, **kwargs):
		form.send_mail()
		return super(IndexView, self).form_valid(form, *args, **kwargs)

	def form_invalid(self, form, *args, **kwargs):
		return super(IndexView, self).form_invalid(form, *args, **kwargs)


# --- Download CV --- #
def download_cv(request):
	file_path = BASE_DIR / 'files/Cv_Antonio_Neves_2021.pdf'

	response = FileResponse(open(file_path, 'rb'))

	return response
