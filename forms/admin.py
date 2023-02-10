from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


class FormsAdmin(ModelAdmin):
    list_display = ['type_project', 'platform', 'project_status', 'start_project', 'name', 'phone', 'email', 'comment',
                    'date_pub']
    search_fields = ['name']


admin.site.register(Form, FormsAdmin)
