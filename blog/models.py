from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField


# --- Category --- #
class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_name = models.CharField('Category', max_length=100, unique=True)
	category_slug = models.SlugField(max_length=150, unique=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
		ordering = ['category_name']

	def __str__(self):
		return self.category_name


# --- Tags --- #
class SubCategory(models.Model):
	sub_category_id = models.AutoField(primary_key=True)
	sub_category_name = models.CharField(
		'Sub Category', max_length=100, unique=True
	)
	sub_category_slug = models.SlugField(max_length=150, unique=True)

	class Meta:
		verbose_name = 'Subcategory'
		verbose_name_plural = 'Subcategories'
		ordering = ['sub_category_name']

	def __str__(self):
		return self.sub_category_name


# --- Article --- #
class Article(models.Model):

	ARTICLE_STATUS = (
		('0', 'Draft'),
		('1', 'Publish')
	)

	article_id = models.AutoField(primary_key=True)
	article_image = CloudinaryField('Image', folder='media/articles/')
	article_cat = models.ForeignKey(
		Category, verbose_name='Category', related_name='articlecategory', on_delete=models.CASCADE)
	article_sub_cat = models.ManyToManyField(
		SubCategory, verbose_name='Tags', related_name='articlesubcategory')
	article_name = models.CharField('Name', max_length=100, unique=True)
	article_slug = models.SlugField(max_length=150, unique=True)
	article_resume = models.CharField('Resume', max_length=200)
	article_content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	article_status = models.CharField(
		max_length=1, choices=ARTICLE_STATUS, default=0
	)

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'
		ordering = ['-modified_at']

	def get_absolute_url(self):
		return reverse('article-detail', args=[self.article_slug])

	def __str__(self):
		return self.article_name
