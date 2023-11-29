# Generated by Django 4.2.5 on 2023-11-28 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okommerce', '0004_product_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_name', to='okommerce.productcategory'),
        ),
    ]
