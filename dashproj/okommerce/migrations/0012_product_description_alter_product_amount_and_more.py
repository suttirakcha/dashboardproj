# Generated by Django 4.2.5 on 2023-12-10 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okommerce', '0011_marketingcampaign_delete_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_sold',
            field=models.BooleanField(),
        ),
    ]
