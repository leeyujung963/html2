from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)