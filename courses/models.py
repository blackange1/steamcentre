from django.db import models


class Courses(models.Model):
    number_of_courses = \
        models.PositiveSmallIntegerField()
    name = \
        models.CharField(max_length=200)
    age_of_student = \
        models.CharField(max_length=50)
    max_count_of_students = \
        models.CharField(max_length=50)
    background_color = \
        models.CharField(max_length=20)
    img_course = \
        models.ImageField(upload_to='courses')
    description = \
        models.TextField()

    def __str__(self):
        return self.name


class ModuleOfCourses(models.Model):
    courses = \
        models.ForeignKey(Courses, on_delete=models.CASCADE)
    name = \
        models.CharField(max_length=200)
    number_of_module = \
        models.PositiveSmallIntegerField()
    description = \
        models.TextField()
    img_module = \
        models.ImageField(upload_to='modules')

    def __str__(self):
        return f'{self.courses.name} | Модуль {self.number_of_module} {self.name}'
