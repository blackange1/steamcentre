import os

from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe


class Laboratory(models.Model):
    number_of_lab = \
        models.PositiveSmallIntegerField()
    name = \
        models.CharField(max_length=200)
    background_color = \
        models.CharField(max_length=20)
    img = \
        models.ImageField(upload_to='labs')
    img_position = \
        models.CharField(
            max_length=10,
            choices=(
                ('left', 'LEFT'),
                ('RIGHT', 'RIGHT'),
            ),
            default='left'
        )
    description = \
        models.TextField()

    def __str__(self):
        return self.name

    @property
    def img_preview(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="120" height="100" />')
        return ""


class Product(models.Model):
    number_of_products = \
        models.PositiveSmallIntegerField()
    lab = \
        models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    name = \
        models.CharField(max_length=200)
    img = \
        models.ImageField(upload_to='products')
    count = \
        models.PositiveSmallIntegerField(null=True, blank=True)
    for_age = \
        models.CharField(max_length=20, null=True, blank=True)
    link_offsite = \
        models.CharField(max_length=255, null=True, blank=True)
    link_protocol = \
        models.CharField(
            max_length=10,
            choices=(
                ('http', 'http'),
                ('https', 'https'),
            ),
            default='https'
        )
    description = \
        models.TextField()

    def __str__(self):
        return self.name

    @property
    def img_preview(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="120" height="100" />')
        return ""


@receiver(models.signals.post_delete, sender=Laboratory)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


@receiver(models.signals.pre_save, sender=Laboratory)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = Laboratory.objects.get(pk=instance.pk).img
    except Laboratory.DoesNotExist:
        return False

    new_file = instance.img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(models.signals.post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


@receiver(models.signals.pre_save, sender=Product)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = Laboratory.objects.get(pk=instance.pk).img
    except Laboratory.DoesNotExist:
        return False

    new_file = instance.img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
