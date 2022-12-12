from django.urls import path

from .views import *

urlpatterns = [
    path('', beautiful_slovenia, name='beautiful_slovenia')
]