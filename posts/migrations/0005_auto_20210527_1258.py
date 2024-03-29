# Generated by Django 3.2 on 2021-05-27 07:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='content_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='content_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_uz',
            field=models.CharField(max_length=250, null=True, verbose_name='title'),
        ),
    ]
