# Generated by Django 4.2.5 on 2023-10-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogadmin', '0004_rename_bloglist_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(error_messages={'required': 'Please fill a title'}, max_length=999, unique=True),
        ),
    ]