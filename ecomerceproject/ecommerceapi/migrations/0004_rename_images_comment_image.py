# Generated by Django 5.0.2 on 2024-02-16 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapi', '0003_product_date_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='images',
            new_name='image',
        ),
    ]
