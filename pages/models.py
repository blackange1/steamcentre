import os

from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe


class Page(models.Model):
    link = \
        models.SlugField(max_length=50, verbose_name='посилання', help_text='Посилання не додається автоматично до меню. Приклад: mobile_lab')
    html_code = \
        models.TextField(
            verbose_name='HTML код сторінки',
            help_text='Контент який буде вставлений між HEADER та FOOTER'
        )

    def __str__(self):
        return self.link


class Image(models.Model):
    name = \
        models.CharField(max_length=50, null=True, blank=True, verbose_name='назва')
    img = \
        models.ImageField(upload_to='pages', verbose_name='зображення')

    date_create = \
        models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.img.url

    @property
    def get_url(self):
        if self.img:
            return f'{self.img.url}'
        return ""

    @property
    def img_preview(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="120" height="100" />')
        return ""


@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


@receiver(models.signals.pre_save, sender=Image)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = Image.objects.get(pk=instance.pk).img
    except Image.DoesNotExist:
        return False

    new_file = instance.img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
