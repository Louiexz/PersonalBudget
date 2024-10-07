from django.urls import path

from personalbudgets.view import *

budgets = [
    path('budget/', BudgetList.as_view(), name='budget-list'),
    path('budget/create/', BudgetCreate.as_view(), name='budget-create'),
    path('budget/update/<uuid:pk>', BudgetUpdate.as_view(), name='budget-update'),
    path('budget/delete/<uuid:pk>/', BudgetDelete.as_view(), name='budget-delete'),
]
goals = [
    path('goals', GoalList.as_view(), name='goal-list'),
    path('goals/create', GoalCreate.as_view(), name='goal-create'),
    path('goals/update/<uuid:pk>', GoalUpdate.as_view(), name='goal-update'),
    path('goals/delete/<uuid:pk>', GoalDelete.as_view(), name='goal-delete'),
    path('goals/add/<uuid:pk>', GoalAdd.as_view(), name='goal-add'),
]
categories = [
    path('categories', CategoryList.as_view(), name='category-list'),
    path('categories/create', CategoryCreate.as_view(), name='category-create'),
    path('categories/update/<uuid:pk>', CategoryUpdate.as_view(), name='category-update'),
    path('categories/delete/<uuid:pk>', CategoryDelete.as_view(), name='category-delete'),
]
transactions = [
    path('transactions', TransactionList.as_view(), name='transaction-list'),
    path('transactions/category/', TransactionList.as_view(), name='transaction-category'),
    path('transactions/create', TransactionCreate.as_view(), name='transaction-create'),
    path('transactions/update/<uuid:pk>', TransactionUpdate.as_view(), name='transaction-update'),
    path('transactions/delete/<uuid:pk>', TransactionDelete.as_view(), name='transaction-delete'),
    path('transactions/paid/<uuid:pk>', TransactionPaid.as_view(), name='transaction-paid'),
]
urlpatterns = [
    path("", SignIn.as_view(), name="sign-in"),
    path("sign-up", SignUp.as_view(), name="sign-up"),

    path("home", HomeView.as_view(), name="home"),
    path("dashboard", PersonalBudgetListView.as_view(), name="dashboard"),
] + budgets + goals + transactions + categories
