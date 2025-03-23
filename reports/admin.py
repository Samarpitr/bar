from django.contrib import admin
from .models import Expense, Income, ExpenseCategory, IncomeCategory


admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
admin.site.register(Expense)
admin.site.register(Income)
