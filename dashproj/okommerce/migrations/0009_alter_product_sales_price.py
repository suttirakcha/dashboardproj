# Generated by Django 4.2.5 on 2023-12-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okommerce', '0008_alter_address_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sales_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
