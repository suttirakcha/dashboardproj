# Generated by Django 4.2.5 on 2023-12-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtemplate', '0005_navbar_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='link',
            field=models.SlugField(default=''),
        ),
    ]
