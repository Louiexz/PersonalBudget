import decimal
from .views import *

from django.views import View
from django.shortcuts import redirect

from ..model import Goal
from ..forms import GoalForm

class GoalList(LoginRequiredMixin, ListView):
    model = Goal
    template_name = "personalbudgets/goal/goal_list.html"

    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return Goal.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = self.get_queryset()
        goal_id = self.request.GET.get("goal")
        if goal_id:
            context['selected_goal'] = get_object_or_404(self.get_queryset(), id=goal_id)
        return context

class GoalCUD():
    model = Goal
    form_class = GoalForm
    success_url = reverse_lazy("goal-list")

    login_url = 'sign-in'  # Define a URL de login

class GoalCreate(LoginRequiredMixin, GoalCUD, CreateView):
    template_name = "personalbudgets/goal/goal_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user  # Atribui o usuário logado
        messages.success(self.request, "Goal created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error creating goal. Please check the details.")
        return super().form_invalid(form)

class GoalUpdate(GoalCUD, UpdateView):
    template_name = "personalbudgets/goal/goal_update.html"

    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return Goal.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Goal updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error updating goal. Please check the details.")
        return super().form_invalid(form)

class GoalDelete(LoginRequiredMixin, DeleteView):
    model = Goal
    template_name = "personalbudgets/goal/goal_delete.html"
    success_url = reverse_lazy("goal-list")

    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return Goal.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        goal_id = self.request.GET.get("goal")
        if goal_id:
            context['selected_goal'] = get_object_or_404(self.get_queryset(), id=goal_id)
        return context
class GoalAdd(LoginRequiredMixin, View):
    def get(self, request, pk):
        goal = get_object_or_404(Goal, pk=pk, user=request.user)
        amount = self.request.GET.get("amount")

        if goal.status == "To Complete":
            goal.pending_amount += decimal.Decimal(amount)
            goal.save()
            messages.success(request, "Goal amount incresed.")
        else:
            messages.warning(request, "Goal is already completed.")

        return redirect("goal-list")