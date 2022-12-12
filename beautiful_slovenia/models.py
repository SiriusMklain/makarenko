from django.db import models


class Article(models.Model):
    location_list = (
        ('right', 'Справа'),
        ('left', 'Слева')
    )
    status_list = (
        ('active', 'Активен'),
        ('dont_active', 'Не активен')
    )
    name = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.FileField(upload_to="image", max_length=100)
    location_image = models.CharField(verbose_name='Положение фото', max_length=250, choices=location_list)
    location_text = models.CharField(verbose_name='Положение текста', max_length=250, choices=location_list)
    status_article = models.CharField(verbose_name='Активно/Не активно', max_length=250, choices=status_list)
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = """Публикация"""
        verbose_name_plural = """Публикации"""

    def __str__(self):
        return self.name