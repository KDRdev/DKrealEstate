from django.contrib import admin
from .models import State


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_short')
    ordering = ('name',)


admin.site.register(State, StateAdmin)