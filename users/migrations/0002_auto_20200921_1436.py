# Generated by Django 2.2.14 on 2020-09-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=50, null=True, verbose_name='last name'),
        ),
    ]