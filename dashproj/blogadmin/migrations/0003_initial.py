# Generated by Django 4.2.5 on 2023-10-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogadmin', '0002_delete_bloglist'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=999)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default=1, max_length=999)),
                ('image', models.ImageField(blank=True, upload_to='posts/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
