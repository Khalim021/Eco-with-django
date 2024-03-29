# Generated by Django 3.2 on 2021-05-27 07:58

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_productmodel_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='title_uz',
            field=models.CharField(max_length=150, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='long_description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='short_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_ru',
            field=models.TextField(null=True, verbose_name='short_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='short_description_uz',
            field=models.TextField(null=True, verbose_name='short_description'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_en',
            field=models.CharField(max_length=512, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_ru',
            field=models.CharField(max_length=512, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='title_uz',
            field=models.CharField(max_length=512, null=True, verbose_name='title'),
        ),
    ]
