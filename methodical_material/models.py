import os

from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe


class Color(models.Model):
    name = \
        models.CharField(max_length=50)

    color = models.CharField(max_length=6, default='0075FF')

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
        models.CharField(max_length=50)

    long_name = \
        models.CharField(max_length=50, null=True, blank=True)

    type_category = \
        models.CharField(
            max_length=10,
            choices=(
                ('урок', 'урок'),
                ('---', '---'),
            ),
            default='---'
        )

    def __str__(self):
        return self.name


class EduMaterial(models.Model):
    name = \
        models.CharField(max_length=200)

    edu_сategory = \
        models.ManyToManyField(EduСategory)

    color = \
        models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)

    img = \
        models.ImageField(upload_to='edu_material')

    date_create = \
        models.DateTimeField(auto_now=True)

    description = \
        models.TextField(null=True, blank=True)

    detailed_description = \
        models.TextField(null=True, blank=True)

    link_download = \
        models.CharField(max_length=255, null=True, blank=True)

    source = \
        models.CharField(max_length=255, null=True, blank=True)

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
