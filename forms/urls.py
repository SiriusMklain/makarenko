from django.urls import path
from .views import *

urlpatterns = [
    path('', MessageForm.as_view(), name='feedback_view'),
]