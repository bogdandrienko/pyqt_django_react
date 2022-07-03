# Generated by Django 4.0.5 on 2022-07-03 05:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(blank=True, default='img/default.jpg', help_text='<small class="text-muted">Изображение</small><hr><br>', null=True, upload_to='img/receipt', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])], verbose_name='Изображение:'),
        ),
    ]
