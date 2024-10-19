from .views import *

from django.views import View
from django.shortcuts import redirect
from dateutil.relativedelta import relativedelta

from ..model import Category, PersonalBudget, Transaction
from personalbudgets.forms import TransactionForm

class TransactionList(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "personalbudgets/transaction/transaction_list.html"

    def get_queryset(self):
        # Filtra as transações do usuário logado
        return Transaction.objects.filter(budget__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        budget_id = self.request.GET.get("budget")
        category_id = self.request.GET.get("category")

        categories = Category.objects.filter(user=self.request.user)

        selected_budget = None
        selected_category = None
        transactions = self.get_queryset()

        if budget_id:
            selected_budget = get_object_or_404(PersonalBudget, id=budget_id, user=self.request.user)
            transactions = self.get_queryset().filter(budget_id=budget_id)
        elif category_id:
            selected_category = get_object_or_404(Category, id=category_id, user=self.request.user)
            transactions = self.get_queryset().filter(category_id=category_id)

        context.update({
            "transactions": transactions,
            "selected_budget": selected_budget,
            "selected_category": selected_category,
            "categories": categories
        })
        return context

class TransactionView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "personalbudgets/transaction/transaction_view.html"

    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return Transaction.objects.filter(budget__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        transaction_id = self.request.GET.get("transaction")
        
        if transaction_id:
            context['selected_transaction'] = get_object_or_404(self.get_queryset(), id=transaction_id)
        else:
            context['selected_transaction'] = None  # Caso não haja transação selecionada

        return context
class TransactionCUD:
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy("transaction-list")

    login_url = 'sign-in'  # Define a URL de login

class TransactionCreate(LoginRequiredMixin, TransactionCUD, CreateView):
    template_name = "personalbudgets/transaction/transaction_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Passa o usuário logado
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user  # Atribui o usuário logado
        messages.success(self.request, "Transaction created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error creating transaction. Please check the details.")
        return super().form_invalid(form)

class TransactionUpdate(LoginRequiredMixin, TransactionCUD, UpdateView):
    template_name = "personalbudgets/transaction/transaction_update.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Passa o usuário logado
        return kwargs

    def get_queryset(self):
        # Filtra as transações do usuário logado
        return Transaction.objects.filter(budget__user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Transaction updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error updating transaction. Please check the details.")
        return super().form_invalid(form)

class TransactionDelete(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = "personalbudgets/transaction/transaction_delete.html"
    success_url = reverse_lazy("transaction-list")

    def get_queryset(self):
        # Filtra as transações do usuário logado
        return Transaction.objects.filter(budget__user=self.request.user)

class TransactionPaid(LoginRequiredMixin, View):
    def get(self, request, pk):
        try:
            transaction = get_object_or_404(Transaction, pk=pk, budget__user=request.user)
            transaction.paid()

            return redirect("transaction-list")
        except Exception as e:
            raise ValueError(e)
