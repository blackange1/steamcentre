# Generated by Django 4.0.4 on 2022-06-22 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('methodical_material', '0007_alter_edumaterial_like'),
        ('users', '0009_subcomment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edu_material',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='methodical_material.edumaterial'),
            preserve_default=False,
        ),
    ]
