# Generated by Django 4.2.5 on 2023-11-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogadmin', '0008_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts'),
        ),
    ]
