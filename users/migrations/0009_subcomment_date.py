# Generated by Django 4.0.4 on 2022-06-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcomment',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
