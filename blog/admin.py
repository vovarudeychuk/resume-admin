from django.contrib import admin
from blog.models import Blog, Category
from django.utils.html import format_html

@admin.register(Blog) 
class BlogAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" height="100"/>'.format(obj.image_src.url))

    image_tag.short_description = 'Image'
    
    list_display = ['title', 'image_tag',]


admin.site.register(Category)
