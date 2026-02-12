# from django.urls import reverse_lazy
# from django.views.generic import FormView
# from principal.forms import ContactForm
#
#
# class ContactFormView(FormView):
# 	form_class = ContactForm
# 	success_url = reverse_lazy('index')
#
# 	def form_valid(self, form, *args, **kwargs):
# 		form.send_mail()
# 		return super().form_valid(form)
#
# 	def form_invalid(self, form, *args, **kwargs):
# 		return super().form_invalid(form)


from django.urls import reverse_lazy
from django.views.generic import FormView
from django.http import JsonResponse
from principal.forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form, *args, **kwargs):
        try:
            form.send_mail()
        except Exception as e:
            if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': str(e)}, status=500)

        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})

        return super().form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'error': 'Invalid form'}, status=400)
        return super().form_invalid(form)
