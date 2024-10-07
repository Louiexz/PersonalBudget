from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

class HomeView(LoginRequiredMixin, ListView):
    template_name = "personalbudgets/home.html"
    login_url = 'sign-in'  # Define a URL de login


    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["username"] = self.request.user

        return context
