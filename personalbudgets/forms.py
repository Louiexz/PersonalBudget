from django import forms

from personalbudgets.model import PersonalBudget, Goal, Transaction
from personalbudgets.model.category_model import Category
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
        fields = ["title", "total_amount", "due_date", "notes"]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category', 'notes']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "budget", "category", "item", "price",
            "remaining_installment", "validity", "notes",
        ]
        widgets = {
            'validity': forms.DateInput(attrs={'type': 'date'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
     
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Pega o usuário do kwargs
        super().__init__(*args, **kwargs)
        
        # Filtra os budgets associados ao usuário logado
        self.fields['budget'].queryset = PersonalBudget.objects.filter(user=user)
        self.fields['category'].queryset = Category.objects.filter(user=user)
