# Generated by Django 3.2 on 2021-05-06 07:56

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productmodel_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='log_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
