from django.contrib import admin
from personalbudgets.model import PersonalBudget, Category, Transaction

admin.site.register(PersonalBudget)
admin.site.register(Category)
admin.site.register(Transaction)
