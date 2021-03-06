# Generated by Django 3.2.6 on 2021-09-15 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100, unique=True, verbose_name='Category')),
                ('category_slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('sub_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(max_length=100, unique=True, verbose_name='Sub Category')),
                ('sub_category_slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
                'ordering': ['sub_category_name'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_image', models.ImageField(upload_to='articles/', verbose_name='Image')),
                ('article_name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('article_slug', models.SlugField(max_length=150, unique=True)),
                ('article_resume', models.CharField(max_length=200, verbose_name='Resume')),
                ('article_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('article_status', models.CharField(choices=[('0', 'Draft'), ('1', 'Publish')], default=0, max_length=1)),
                ('article_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articlecategory', to='blog.category', verbose_name='Category')),
                ('article_sub_cat', models.ManyToManyField(related_name='articlesubcategory', to='blog.SubCategory', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['article_name'],
            },
        ),
    ]
