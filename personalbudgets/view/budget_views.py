from .views import *

from ..model import PersonalBudget
from ..forms import BudgetForm

class BudgetList(LoginRequiredMixin, ListView):
    model = PersonalBudget
    template_name = "personalbudgets/budget/budget_list.html"

    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return PersonalBudget.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['budgets'] = self.get_queryset()
        budget_id = self.request.GET.get("budget")
        
        if budget_id:
            context['selected_budget'] = get_object_or_404(self.get_queryset(), id=budget_id)
        return context

class BudgetCUD():
    model = PersonalBudget
    form_class = BudgetForm
    success_url = reverse_lazy("budget-list")

    login_url = 'sign-in'  # Define a URL de login

class BudgetCreate(LoginRequiredMixin, BudgetCUD, CreateView):
    template_name = "personalbudgets/budget/budget_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user  # Atribui o usuário logado
        messages.success(self.request, "Budget created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error creating budget. Please check the details.")
        return super().form_invalid(form)

class BudgetUpdate(BudgetCUD, UpdateView):
    template_name = "personalbudgets/budget/budget_update.html"

    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return PersonalBudget.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Budget updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error updating budget. Please check the details.")
        return super().form_invalid(form)

class BudgetDelete(LoginRequiredMixin, DeleteView):
    model = PersonalBudget
    template_name = "personalbudgets/budget/budget_delete.html"
    success_url = reverse_lazy("budget-list")

    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return PersonalBudget.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        budget_id = self.request.GET.get("budget")
        if budget_id:
            context['selected_budget'] = get_object_or_404(PersonalBudget, id=budget_id, user=self.request.user)
        return context
