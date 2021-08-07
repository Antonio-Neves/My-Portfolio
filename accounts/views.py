from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from accounts.models import CustomUser
from django.contrib.auth.views import (
	LoginView,
	PasswordChangeView,
	PasswordResetView,
	PasswordResetConfirmView,
	PasswordResetCompleteView,
	)


class UserLogin(SuccessMessageMixin, LoginView):
	redirect_authenticated_user = True
	template_name = 'accounts/login.html'


class UserCreate(SuccessMessageMixin, CreateView):
	model = CustomUser
	form_class = CustomUserCreateForm
	template_name = 'accounts/user-new.html'
	success_url = reverse_lazy('login')
	success_message = 'Welcome! Log in to start'

	def get(self, request, *args, **kwargs):

		if request.user.is_authenticated:
			return redirect('index')

		else:
			return super().get(request, *args, **kwargs)


class UserChange(SuccessMessageMixin, UpdateView):
	model = CustomUser
	form_class = CustomUserChangeForm
	template_name = 'accounts/user-change.html'
	success_url = reverse_lazy('index')
	success_message = 'Your profile change was successful'

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return self.model.objects.filter(username=self.request.user)

		else:
			return super().get_queryset().filter(username=None)


class UserDelete(SuccessMessageMixin, DeleteView):
	model = CustomUser
	success_url = reverse_lazy('index')
	template_name = 'accounts/user-delete.html'

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return self.model.objects.filter(username=self.request.user)

		else:
			return super().get_queryset().filter(username=None)


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
	template_name = 'accounts/password-change.html'
	success_url = reverse_lazy('index')
	success_message = 'Your password change was successful'


class PasswordReset(SuccessMessageMixin, PasswordResetView):
	template_name = 'accounts/password-reset.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
	success_message = 'Your password has been reset correctly. Log in to start'


class PasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
	template_name = 'accounts/password-reset-complete.html'
	success_message = 'Your password has been reset correctly. Log in to start'

	# For use with a html template, don't subscrive the 'get' method
	# and use the template 'template_name = '
	def get(self, request, *args, **kwargs):

		return redirect('login')
