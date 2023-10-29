from django.contrib import admin
from .models import Category, Post

@admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publish_time', 'status')