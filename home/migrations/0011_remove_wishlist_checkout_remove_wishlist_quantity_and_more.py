# Generated by Django 4.1.5 on 2023-02-17 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='checkout',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='total',
        ),
    ]