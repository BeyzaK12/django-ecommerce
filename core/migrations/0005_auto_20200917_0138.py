# Generated by Django 2.2.14 on 2020-09-17 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='coupon',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='refund',
            name='order',
        ),
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='one_click_purchasing',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='stripe_customer_id',
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('A', 'Atıştırmalık'), ('I', 'İçecek'), ('D', 'Dondurulmuş'), ('K', 'Kuru')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Refund',
        ),
    ]