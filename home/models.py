from django.db import models


class Project(models.Model):
    status_list = (
        ('active', 'Активный'),
        ('completed', 'Архивный')
    )
    status = models.CharField(verbose_name='Статус проекта', max_length=250, choices=status_list)
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание проекта")
    image = models.ImageField(upload_to="media/project/")
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = """Проект"""
        verbose_name_plural = """Проекты"""

    def __str__(self):
        return self.name


class Form(models.Model):
    type = models.CharField(verbose_name='Тип проекта', max_length=250)
    platform = models.CharField(verbose_name='Платформа проекта', max_length=250)
    condition = models.CharField(verbose_name='Состояние проекта', max_length=250)
    when = models.CharField(verbose_name='Когда начать проект', max_length=250)
    name = models.CharField(verbose_name='Имя заказчика', max_length=250)
    phone = models.CharField(verbose_name='Телефон заказчика', max_length=250)
    email = models.CharField(verbose_name='Email заказчика', max_length=250)
    comment = models.CharField(verbose_name='Комметнарий заказчика', max_length=250)
    file = models.FileField(upload_to="media/form/")

    class Meta:
        verbose_name = """Заявка"""
        verbose_name_plural = """Заявки"""

    def __str__(self):
        return self.name