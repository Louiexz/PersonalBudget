from django import forms

from personalbudgets.model import PersonalBudget, Goal, Transaction
from personalbudgets.model.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = PersonalBudget
        fields = ["budget", "total_amount", "validity", "notes"]
        widgets = {
            'validity': forms.DateInput(attrs={'type': 'date'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ["title", "due_date", "notes"]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "category", "item", "price",
            "remaining_installment", "validity", "notes",
        ]
        widgets = {
            'validity': forms.DateInput(attrs={'type': 'date'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }