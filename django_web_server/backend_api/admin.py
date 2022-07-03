from django.contrib import admin

from . import models

# Register your models here.

admin.site.site_header = 'Панель управления приложением'
admin.site.index_title = 'Управление моделями!'
admin.site.site_title = 'Панель'


class ImageModelAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'ImageModel' на панели администратора
    """

    list_display = (
        'title',
        'image',
    )
    list_display_links = (
        'title',
    )
    list_editable = (
    )
    list_filter = (
        'title',
        'image',
    )
    fieldsets = (
        ('Основное', {'fields': (
            'title',
        )}),
        ('Дополнительно', {'fields': (
            'image',
        )}),
    )
    search_fields = [
        'title',
        'image',
    ]


admin.site.register(models.ImageModel, ImageModelAdmin)
