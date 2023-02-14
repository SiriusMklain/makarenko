# Generated by Django 4.1.3 on 2023-02-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_project', models.CharField(max_length=255, verbose_name='Тип проекта')),
                ('platform', models.CharField(max_length=255, verbose_name='Тип проекта')),
                ('project_status', models.CharField(max_length=255, verbose_name='Тип проекта')),
                ('start_project', models.CharField(max_length=255, verbose_name='Тип проекта')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='E-mail')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
            options={
                'verbose_name': 'Заявка на сайте',
                'verbose_name_plural': 'Заявки на сайте',
            },
        ),
    ]