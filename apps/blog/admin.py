from django.contrib import admin

# Register your models here.
from apps.blog.models import Category, Post, Tag


@admin.register(Tag)
class TafAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","created", "category", "is_draft"]
    list_filter = ["category", "is_draft", "created", ]
    filter_horizontal = ["tags"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ["name", "slug","id"]

