# Generated by Django 4.0.4 on 2022-05-31 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_courses_img_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='name',
            new_name="ім'я",
        ),
    ]
