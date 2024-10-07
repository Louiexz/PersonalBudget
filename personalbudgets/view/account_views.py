from .views import *

from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ..forms import UserRegistrationForm

class SignIn(View):
    template_name = "personalbudgets/account/sign_in.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.warning(request, "Username or password is incorrect.")
            return render(request, self.template_name)

class SignUp(CreateView):
    form_class = UserRegistrationForm
    template_name = "personalbudgets/account/sign_up.html"
    success_url = reverse_lazy("sign_in")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Criptografa a senha
        user.save()
        messages.success(self.request, "Registration successful! Please log in.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error sending the form. Check the data and try again.")
        return super().form_invalid(form)
