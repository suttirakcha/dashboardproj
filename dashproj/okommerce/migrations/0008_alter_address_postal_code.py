# Generated by Django 4.2.5 on 2023-11-30 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okommerce', '0007_alter_address_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]