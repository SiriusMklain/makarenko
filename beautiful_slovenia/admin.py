from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


class ArticleAdmin(ModelAdmin):
    list_display = [
                    'name',
                    'location_image',
                    'location_text',
                    'status_article',
                    'date_pub',
                    ]
    search_fields = ['name']

admin.site.register(Article, ArticleAdmin)
