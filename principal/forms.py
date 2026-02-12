# from django import forms
# from django_recaptcha.fields import ReCaptchaField
# from django_recaptcha.widgets import ReCaptchaV2Checkbox
# from django.core.mail.message import EmailMessage
# from decouple import config
#
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
#
#
# class ContactForm(forms.Form):
# 	contact_name = forms.CharField(max_length=100)
# 	contact_email = forms.CharField(max_length=100)
# 	contact_message = forms.CharField(widget=forms.Textarea())
#
# 	def send_mail(self):
#
# 		contact_name = self.cleaned_data['contact_name']
# 		contact_email = self.cleaned_data['contact_email']
# 		contact_message = self.cleaned_data['contact_message']
#
# 		contact_content = 'Name: {}\nEmail: {}\nMessage: {}'\
# 			.format(contact_name, contact_email, contact_message)
#
# 		mail = EmailMessage(
# 			subject='Email from My Portfolio',
# 			body=contact_content,
# 			from_email=EMAIL_HOST_USER,
# 			to=[EMAIL_HOST_USER,],
# 			headers={'Reply-to': contact_email}
# 		)
# 		mail.send()
#
# 	captcha = ReCaptchaField(
# 		widget=ReCaptchaV2Checkbox(
#         attrs={
#             'data-theme': 'dark',
#             # 'data-size': 'compact',
#         })
#         )


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
            "from": "Portfolio <resend@aninformatica.com>",
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