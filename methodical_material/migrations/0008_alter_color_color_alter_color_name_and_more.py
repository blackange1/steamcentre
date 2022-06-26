# Generated by Django 4.0.4 on 2022-06-26 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('methodical_material', '0007_alter_edumaterial_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(default='0075FF', help_text='Значення даного поля має бути записане в 16-й системі, #(решітку) прописувати не варто. Приклад: ff00ee', max_length=6, verbose_name='колір'),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(help_text='Значення даного поля відображається лише в адмінці', max_length=50, verbose_name='назва'),
        ),
        migrations.AlterField(
            model_name='edumaterial',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='methodical_material.color', verbose_name='колір'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='edumaterial',
            name='description',
            field=models.TextField(blank=True, help_text='Короткий опис матеріалу', null=True, verbose_name='опис'),
        ),
        migrations.AlterField(
            model_name='edumaterial',
            name='detailed_description',
            field=models.TextField(blank=True, help_text='Детальний опис матеріалу. Якщо залишити поле пустим, то в деталях матеріалу використовуватиметься опис той, що звурху', null=True, verbose_name='опис з використанням HTML'),
        ),
        migrations.AlterField(
            model_name='edumaterial',
            name='edu_сategory',
            field=models.ManyToManyField(to='methodical_material.eduсategory', verbose_name='категорії'),
        ),
        migrations.AlterField(
            model_name='edumaterial',
            name='img',
            field=models.ImageField(upload_to='edu_material', verbose_name='зображення'),
        ),
        migrations.AlterField(
            model_name='edumaterial',
            name='link_download',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='посилання для скачування'),
        ),
        migrations.AlterField(
            model_name='edumaterial',
            name='name',
            field=models.CharField(max_length=200, verbose_name='назва'),
        ),
        migrations.AlterField(
            model_name='edumaterial',
            name='source',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='посилання на оригінал'),
        ),
        migrations.AlterField(
            model_name='eduсategory',
            name='long_name',
            field=models.CharField(blank=True, help_text='\n                Використовується у меню те, що зправа. Якщо ви бажаєте, \n                щоб "коротка назва" співпадала з "довгою назвою", залиште це поле пустим. Приклад: JavaScript.\n            ', max_length=50, null=True, verbose_name='довга назва'),
        ),
        migrations.AlterField(
            model_name='eduсategory',
            name='name',
            field=models.CharField(help_text='Використовується у фільрах матеріалів.Приклад: JS.', max_length=50, verbose_name='коротка назва'),
        ),
        migrations.AlterField(
            model_name='eduсategory',
            name='type_category',
            field=models.CharField(choices=[('урок', 'урок'), ('---', '---')], default='---', help_text='Всі назви предметів слід додавати до типу "Урок"', max_length=10, verbose_name='тип категорії'),
        ),
    ]