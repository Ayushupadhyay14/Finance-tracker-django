from django.contrib import admin
# it use to show data on admin pannele
from finance.models import Transaction, Goal
# Register your models here.

admin.site.register(Transaction)
admin.site.register(Goal)
