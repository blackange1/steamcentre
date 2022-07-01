import os

from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe


class Courses(models.Model):

    class Meta:
        verbose_name_plural = 'Курси'

    number_of_courses = \
        models.PositiveSmallIntegerField(
            verbose_name='номер',
            help_text="""
                Для кожного курсу номер має бути унікальний,
                 показ курсів відбувається за зростанням даного номеру.
            """
        )
    name = \
        models.CharField(max_length=200, verbose_name='назва')

    age_of_student = \
        models.CharField(
            max_length=50,
            verbose_name='вік учнів',
            help_text="Приклад: 9-10 років"
        )

    max_count_of_students = \
        models.CharField(
            max_length=50,
            verbose_name='максимальна кількість учнів',
            help_text="Максимальна кількість яка може навчатись на цьому курсі. Приклад: 8 учнів"
        )

    background_color = \
        models.CharField(
            max_length=6,
            help_text='Значення даного поля має бути записане в 16-й системі, #(решітку) прописувати не варто. Приклад: ff00ee',
            verbose_name='Колір фону'
        )

    img_course = \
        models.ImageField(upload_to='courses', verbose_name='Зодраження')

    description = \
        models.TextField(verbose_name='Опис')

    def __str__(self):
        return self.name

    @property
    def img_preview(self):
        if self.img_course:
            return mark_safe(f'<img src="{self.img_course.url}" width="120" height="100" />')
        return ""


class ModuleOfCourses(models.Model):

    class Meta:
        verbose_name_plural = 'Модулі курсів'

    courses = \
        models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='курс')

    name = \
        models.CharField(max_length=200, verbose_name='назва')

    number_of_module = \
        models.PositiveSmallIntegerField(
            verbose_name='номер',
            help_text='Для кожного модуля в курсі номер має бути унікальний, показ модулів відбувається за зростанням даного номеру.'
        )

    description = \
        models.TextField(verbose_name='опис', help_text='Кожна нова тема має бути введена з нового рядка')

    img_module = \
        models.ImageField(upload_to='modules', verbose_name='зображення')

    def __str__(self):
        return f'{self.courses.name} | Модуль {self.number_of_module} {self.name}'

    @property
    def img_preview(self):
        if self.img_module:
            return mark_safe(f'<img src="{self.img_module.url}" width="100" height="100" />')
        return ""


@receiver(models.signals.post_delete, sender=Courses)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.img_course:
        if os.path.isfile(instance.img_course.path):
            os.remove(instance.img_course.path)


@receiver(models.signals.pre_save, sender=Courses)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = Courses.objects.get(pk=instance.pk).img_course
    except Courses.DoesNotExist:
        return False

    new_file = instance.img_course
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(models.signals.post_delete, sender=ModuleOfCourses)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.img_module:
        if os.path.isfile(instance.img_module.path):
            os.remove(instance.img_module.path)


@receiver(models.signals.pre_save, sender=ModuleOfCourses)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = ModuleOfCourses.objects.get(pk=instance.pk).img_module
    except ModuleOfCourses.DoesNotExist:
        return False

    new_file = instance.img_module
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
