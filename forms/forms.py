from django import forms
from .models import *


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Form
        type_project_list = (
            ('e-commerce', 'Электронная коммерция'),
            ('customer_service', 'Обслуживание клиентов'),
            ('intranet', 'Интранет'),
            ('big_bata', 'Big Data'),
            ('another', 'Другое')
        )
        platform_list = (
            ('responsive_website', 'Адаптивный сайт'),
            ('mobile_app', 'Мобильное приложение')
        )
        project_status_list = (
            ('new_project', 'Новый проект'),
            ('existing_project', 'Существующий проект')
        )
        start_project_list = (
            ('immediately', 'Немедленно'),
            ('in_week', 'В течение недели'),
            ('in_month', 'В течение месяца'),
        )
        fields = ['type_project', 'platform', 'project_status', 'start_project', 'name', 'phone', 'email', 'comment', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'required', 'id': 'name'}),
            'phone': forms.TextInput(attrs={'class': 'required', 'id': 'phone', 'type': 'tel'}),
            'email': forms.TextInput(attrs={'class': 'required email', 'id': 'email'}),
            'inn': forms.TextInput(attrs={'id': 'inn', 'class': 'inn'}),
            'name_debt': forms.TextInput(attrs={'class': 'form-group', 'id': 'name_debt'}),
            'sud': forms.Select(),
            'sum_debt': forms.TextInput(attrs={'class': 'form-group', 'id': 'sum_debt'}),
            'list': forms.Select(),
        }
