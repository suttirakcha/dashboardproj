# Generated by Django 4.2.5 on 2023-11-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okommerce', '0006_promotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.IntegerField(blank=True),
        ),
    ]
