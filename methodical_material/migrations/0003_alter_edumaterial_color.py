# Generated by Django 4.0.4 on 2022-05-31 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('methodical_material', '0002_color_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edumaterial',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='methodical_material.color'),
        ),
    ]
