# Generated by Django 2.2.14 on 2020-09-21 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200921_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ürün',
            name='description',
        ),
        migrations.RemoveField(
            model_name='ürün',
            name='discount_price',
        ),
        migrations.RemoveField(
            model_name='ürün',
            name='image',
        ),
        migrations.RemoveField(
            model_name='ürün',
            name='price',
        ),
        migrations.RemoveField(
            model_name='ürün',
            name='title',
        ),
    ]