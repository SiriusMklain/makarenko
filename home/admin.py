from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


class ProjectAdmin(ModelAdmin):
    list_display = ['name', 'status', 'date_pub']
    search_fields = ['name']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Form)
