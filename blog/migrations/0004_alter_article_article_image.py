# Generated by Django 5.1.1 on 2024-10-05 12:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image'),
        ),
    ]
