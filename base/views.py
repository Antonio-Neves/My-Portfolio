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


from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from decouple import config
import resend

resend.api_key = config('RESEND_API_KEY')


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=100)
    contact_email = forms.CharField(max_length=100)
    contact_message = forms.CharField(widget=forms.Textarea())

    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
            }
        )
    )

    def send_mail(self):
        contact_name = self.cleaned_data['contact_name']
        contact_email = self.cleaned_data['contact_email']
        contact_message = self.cleaned_data['contact_message']

        params: resend.Emails.SendParams = {
            "from": "Portfolio <no_exists@aninformatica.com>",
            "to": ["myportfolio@aninformatica.com"],
            "reply_to": contact_email,
            "subject": f"New message from {contact_name}",
            "html": f"""
                <h2>New contact from Portfolio</h2>
                <p><strong>Name:</strong> {contact_name}</p>
                <p><strong>Email:</strong> {contact_email}</p>
                <p><strong>Message:</strong></p>
                <p>{contact_message}</p>
            """,
        }

        resend.Emails.send(params)