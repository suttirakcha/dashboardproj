# Generated by Django 4.2.5 on 2023-12-12 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okommerce', '0013_remove_product_is_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='okommerz'),
        ),
    ]
