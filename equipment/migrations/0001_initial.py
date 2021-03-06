# Generated by Django 4.0.4 on 2022-05-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_lab', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('background_color', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='labs')),
                ('description', models.TextField()),
            ],
        ),
    ]
