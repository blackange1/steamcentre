# Generated by Django 4.0.4 on 2022-05-31 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('methodical_material', '0005_alter_eduсategory_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='edumaterial',
            name='like',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
