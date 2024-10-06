from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy