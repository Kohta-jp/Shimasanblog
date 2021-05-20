from django.contrib import admin

# Register your models here.
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from blog.models import Category, Tag, Post

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, MarkdownxModelAdmin)
