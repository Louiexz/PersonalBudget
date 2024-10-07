from personalbudgets.forms import CategoryForm
from .views import *

from ..model import Category
class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    template_name = "personalbudgets/category/category_list.html"

    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return Category.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_queryset()
        category_id = self.request.GET.get("category")
        if category_id:
            context['selected_category'] = get_object_or_404(self.get_queryset(), id=category_id)
        return context

class CategoryCUD():
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("category-list")
    login_url = 'sign-in'  # Define a URL de login

class CategoryCreate(LoginRequiredMixin, CategoryCUD, CreateView):
    template_name = "personalbudgets/category/category_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user  # Atribui o usuário logado
        messages.success(self.request, "Category created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error creating category. Please check the details.")
        return super().form_invalid(form)

class CategoryUpdate(CategoryCUD, UpdateView):
    template_name = "personalbudgets/category/category_update.html"

    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return Category.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Category updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error updating category. Please check the details.")
        return super().form_invalid(form)

class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "personalbudgets/category/category_delete.html"
    success_url = reverse_lazy("category-list")

    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return Category.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.request.GET.get("category")
        if category_id:
            context['selected_category'] = get_object_or_404(Category, id=category_id, user=self.request.user)
        return context
