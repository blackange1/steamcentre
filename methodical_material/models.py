import os

from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe


class Color(models.Model):
    name = \
        models.CharField(
            max_length=50,
            verbose_name='назва',
            help_text='Значення даного поля відображається лише в адмінці'
        )

    color = models.CharField(
        max_length=6,
        default='0075FF',
        verbose_name='колір',
        help_text='Значення даного поля має бути записане в 16-й системі, #(решітку) прописувати не варто. Приклад: ff00ee'
    )

    def __str__(self):
        return self.name

    @property
    def color_preview(self):
        style = f'background: #{self.color}; padding: 10px;'
        if self.color:
            return mark_safe(f'<div style="{style}">{self.color}</div>')
        return ""


class EduСategory(models.Model):
    name = \
        models.CharField(
            max_length=50,
            verbose_name='коротка назва',
            help_text='Використовується у фільрах матеріалів.Приклад: JS.'
        )

    long_name = \
        models.CharField(
            max_length=50,
            null=True,
            blank=True,
            verbose_name='довга назва',
            help_text="""
                Використовується у меню те, що зправа. Якщо ви бажаєте, 
                щоб "коротка назва" співпадала з "довгою назвою", залиште це поле пустим. Приклад: JavaScript.
            """
        )

    type_category = \
        models.CharField(
            max_length=10,
            choices=(
                ('урок', 'урок'),
                ('---', '---'),
            ),
            default='---',
            verbose_name='тип категорії',
            help_text='Всі назви предметів слід додавати до типу "Урок"'
        )

    def __str__(self):
        return self.name


class EduMaterial(models.Model):
    name = \
        models.CharField(max_length=200, verbose_name='назва')

    edu_сategory = \
        models.ManyToManyField(EduСategory, verbose_name='категорії')

    color = \
        models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True, verbose_name='колір')

    img = \
        models.ImageField(upload_to='edu_material', verbose_name='зображення')

    date_create = \
        models.DateTimeField(auto_now=True)

    description = \
        models.TextField(
            null=True,
            blank=True,
            verbose_name='опис',
            help_text='Короткий опис матеріалу'
        )

    detailed_description = \
        models.TextField(
            null=True,
            blank=True,
            verbose_name='опис з використанням HTML',
            help_text='Детальний опис матеріалу. Якщо залишити поле пустим, то в деталях матеріалу використовуватиметься опис той, що звурху'
        )

    link_download = \
        models.CharField(max_length=255, null=True, blank=True, verbose_name='посилання для скачування')

    source = \
        models.CharField(max_length=255, null=True, blank=True, verbose_name='посилання на оригінал')

    like = \
        models.PositiveIntegerField(default=0)

    @property
    def img_preview(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="120" height="100" />')
        return ""

    def __str__(self):
        return self.name


@receiver(models.signals.post_delete, sender=EduMaterial)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


@receiver(models.signals.pre_save, sender=EduMaterial)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = EduMaterial.objects.get(pk=instance.pk).img
    except EduMaterial.DoesNotExist:
        return False

    new_file = instance.img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
