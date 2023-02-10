from django.db import models


class Form(models.Model):
    """Form"""
    type_project = models.CharField(max_length=255, verbose_name="Тип проекта")
    platform = models.CharField(max_length=255, verbose_name="Платформа проекта")
    project_status = models.CharField(max_length=255, verbose_name="Статус проекта")
    start_project = models.CharField(max_length=255, verbose_name="Старт проекта")
    name = models.CharField(max_length=255, verbose_name="Имя")
    phone = models.CharField(max_length=255, verbose_name="Телефон", blank=True, null=True)
    email = models.CharField(max_length=255, verbose_name="E-mail", blank=True, null=True)
    comment = models.TextField(verbose_name="Комментарий", blank=True, null=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    date_pub = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Заявка на сайте'
        verbose_name_plural = 'Заявки на сайте'
