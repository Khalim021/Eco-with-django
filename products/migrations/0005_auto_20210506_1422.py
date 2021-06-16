# Generated by Django 3.2 on 2021-05-06 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productmodel_log_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.brandmodel'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.categorymodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='products', to='products.ProductTagModel'),
        ),
    ]
