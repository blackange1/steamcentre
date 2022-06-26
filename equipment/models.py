import os

from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe


class Laboratory(models.Model):
    number_of_lab = \
        models.PositiveSmallIntegerField(
            verbose_name='номер',
            help_text='Для кожногї лабораторії номер має бути унікальний, показ лаболаторій відбувається за зростанням даного номеру.'
        )
    name = \
        models.CharField(max_length=200, verbose_name='назва')
    background_color = \
        models.CharField(
            max_length=20,
            verbose_name='колір фону',
            help_text='Значення даного поля має бути записане в 16-й системі, #(решітку) прописувати не варто. Приклад: ff00ee'
        )
    img = \
        models.ImageField(upload_to='labs', verbose_name='зображення')
    img_position = \
        models.CharField(
            max_length=10,
            choices=(
                ('left', 'ліворуч'),
                ('right', 'праворуч'),
            ),
            default='left',
            verbose_name='Розміщення'
        )
    description = \
        models.TextField(verbose_name='опис')

    def __str__(self):
        return self.name

    @property
    def img_preview(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" width="120" height="100" />')
        return ""


class Product(models.Model):
    number_of_products = \
        models.PositiveSmallIntegerField(
            verbose_name='номер',
            help_text='Для кожного набору номер має бути унікальний, показ наборів відбувається за зростанням даного номеру.'
        )

    name = \
        models.CharField(max_length=200, verbose_name='назва')

    lab = \
        models.ForeignKey(Laboratory, on_delete=models.CASCADE, verbose_name='Лоболаторія')

    img = \
        models.ImageField(upload_to='products', verbose_name='Зображення')
    count = \
        models.PositiveSmallIntegerField(
            null=True,
            blank=True,
            verbose_name='Кількість',
            help_text="Мається на увазі кількість працюючих наборів. Приклад: 5"
        )
    for_age = \
        models.CharField(
            max_length=20,
            null=True,
            blank=True,
            verbose_name='Допустимий вік',
            help_text="Приклад: від 4 до 12 років.",
        )
    link_offsite = \
        models.CharField(
            max_length=255,
            null=True,
            blank=True,
            verbose_name='Посилання на офіційний сайт',
            help_text='посилання без врахування протоколу. Приклад: matatalab.com/en'
        )
    link_protocol = \
        models.CharField(
            max_length=10,
            choices=(
                ('http', 'http'),
                ('https', 'https'),
            ),
            default='https',
            verbose_name='Протокол офіційного сайту'
        )
    description = \
        models.TextField(
            verbose_name='Опис',
            help_text='Дане поле розуміє HTML та використовується для відображення вмісту модального вікна при натисканні на набір'
        )

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
        old_file = Product.objects.get(pk=instance.pk).img
    except Product.DoesNotExist:
        return False

    new_file = instance.img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
