from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(CustomerAccounts)
admin.site.register(BankAccounts)
admin.site.register(ExpenseCategory)