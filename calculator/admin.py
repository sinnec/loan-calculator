from django.contrib import admin
from .models import Plan

# Register your models here.
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'available_plans', 'amount', 'months')
    ordering = ('class_name',)