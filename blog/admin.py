from django.contrib import admin
from .models import Article, Category, Tag, Comment
# Register your models here.


class CommentItemInLine(admin.TabularInline):
    model = Comment
    raw_id_fields = ['article']


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'category__name', 'tags__name']
    list_display = ['title', 'category', 'created_at', 'updated_at']
    list_filter = ['category', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentItemInLine]


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name', )}


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'content', 'email', 'article__title']
    list_display = ['name', 'created_at', 'email', 'content', 'article']
    list_filter = ['name', 'created_at', 'email', 'article']


class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_filter = ['name']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
