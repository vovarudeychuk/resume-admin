from django.utils.html import format_html
from django.contrib import admin
from import_export.admin import ImportExportMixin

from mixins.active import ActivateDeactivateMixin

from .models import Portfolio, Project, Category

class PortfolioAdmin(ActivateDeactivateMixin, ImportExportMixin, admin.ModelAdmin):
    list_display = ('title', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
    actions = ['make_active', 'make_inactive']
    
# Register your models here.
@admin.register(Project) 
class ProjectAdmin(ImportExportMixin, admin.ModelAdmin):
    
    def image_tag(self, obj):
        return format_html('<img src="{}" height="100"/>'.format(obj.image_src.url))
    
    image_tag.short_description = 'Image'
    
    list_display = ('title', 'image_tag',)

# admin.site.register(Project, ProjectAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category)

