from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models import Category, SubCategory, Article


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'category_slug': ('category_name',)}


class SubCategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'sub_category_slug': ('sub_category_name',)}


class ArticleAdmin(SummernoteModelAdmin):
	list_display = ['article_name', 'article_cat', 'modified_at', 'article_status']
	list_filter = ('article_cat', 'article_sub_cat', 'article_status')
	search_fields = ['article_name']
	list_editable = ['article_status']
	radio_fields = {'article_status': admin.HORIZONTAL}
	prepopulated_fields = {'article_slug': ('article_name',)}
	summernote_fields = ('article_content',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
