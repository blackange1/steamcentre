import os

from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe


class MainSlider(models.Model):
    title = \
        models.CharField(max_length=200)
    text = \
        models.TextField()
    img = \
        models.ImageField(upload_to='main_slider')

    def __str__(self):
        return self.title

    @property
    def img_preview(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="100" height="100" />')
        return ""


@receiver(models.signals.post_delete, sender=MainSlider)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


@receiver(models.signals.pre_save, sender=MainSlider)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = MainSlider.objects.get(pk=instance.pk).img
    except MainSlider.DoesNotExist:
        return False

    new_file = instance.img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
