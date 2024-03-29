# Generated by Django 3.2 on 2021-05-25 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_contactmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='message',
            field=models.TextField(verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
    ]
