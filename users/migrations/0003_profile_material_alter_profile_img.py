# Generated by Django 4.0.4 on 2022-06-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('methodical_material', '0007_alter_edumaterial_like'),
        ('users', '0002_comment_subcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='material',
            field=models.ManyToManyField(to='methodical_material.edumaterial'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='user_photos'),
        ),
    ]
