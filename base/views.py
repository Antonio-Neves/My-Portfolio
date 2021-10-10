from django.urls import reverse_lazy
from django.views.generic import FormView
from principal.forms import ContactForm


class ContactFormView(FormView):
	form_class = ContactForm
	success_url = reverse_lazy('index')

	def form_valid(self, form, *args, **kwargs):
		form.send_mail()
		return super().form_valid(form)

	def form_invalid(self, form, *args, **kwargs):
		return super().form_invalid(form)
