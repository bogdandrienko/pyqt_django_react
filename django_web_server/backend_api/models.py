from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class ImageModel(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Заголовок",
        verbose_name="Заголовок:",
        help_text='<small class="text-muted">Заголовок</small><hr><br>',

        max_length=250,
    )
    image = models.ImageField(
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="img/default.jpg",
        verbose_name="Изображение:",
        help_text='<small class="text-muted">Изображение</small><hr><br>',

        validators=[FileExtensionValidator(['jpg', 'png'])],
        upload_to='img/receipt',
        max_length=100,
    )

    class Meta:
        app_label = 'backend_api'
        ordering = ('title',)
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.title}'
