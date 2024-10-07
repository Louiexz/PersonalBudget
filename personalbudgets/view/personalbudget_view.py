from .views import *

from django.db.models import Sum
from ..model import PersonalBudget, Goal

class PersonalBudgetListView(LoginRequiredMixin, ListView):
    model = PersonalBudget
    login_url = 'sign-in'  # Define a URL de login

    def get_queryset(self):
        # Filtra os orçamentos do usuário logado
        return PersonalBudget.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Usuário logado
        username = self.request.user

        # Calcular totais agregados apenas para os budgets do usuário
        total_budgets = self.get_queryset().count()
        total_amount = self.get_queryset().aggregate(total_amount=Sum("total_amount"))["total_amount"] or 0
        
        total_spent = self.get_queryset().aggregate(total_spent=Sum("total_spent"))["total_spent"] or 0
        total_remaining = total_amount - total_spent

        context["budgets"] = {
            "username": username,
            "total_budgets": total_budgets,
            "total_amount": total_amount,
            "total_spent": total_spent,
            "total_remaining": total_remaining,
        }

        # Calcular totais agregados apenas para os goals do usuário
        goal = Goal.objects.filter(user=self.request.user)

        count = goal.count()
        total_goals = count if count > 0 else 0
        goal_total_amount = goal.aggregate(total_amount=Sum("total_amount"))["total_amount"] or 0
        
        pending_amount = goal.aggregate(pending_amount=Sum("pending_amount"))["pending_amount"] or 0
        goal_total_remaining = goal_total_amount - pending_amount 

        context["goals"] = {
            "total_goals": total_goals,
            "total_amount": goal_total_amount,
            "pending_amount": pending_amount,
            "total_remaining": goal_total_remaining,
        }

        return context
