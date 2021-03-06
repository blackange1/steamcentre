# Generated by Django 4.0.4 on 2022-05-26 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_courses', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('age_of_student', models.CharField(max_length=50)),
                ('max_count_of_students', models.CharField(max_length=50)),
                ('background_color', models.CharField(max_length=20)),
                ('img_course', models.ImageField(upload_to='courses')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ModuleOfCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number_of_module', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('img_module', models.ImageField(default='', null=True, upload_to='modules')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
            ],
        ),
    ]
