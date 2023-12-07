from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportMixin


from mixins.active import ActivateDeactivateMixin

from .models import About, Client, Service, Testimonial


@admin.register(About)
class AboutAdmin(ActivateDeactivateMixin, ImportExportMixin, admin.ModelAdmin):
    def display_clients_count(self, obj):
       return str(obj.clients.count())

    display_clients_count.short_description = 'Clients'
    
    def display_services_count(self, obj):
       return str(obj.services.count())

    display_services_count.short_description = 'Services'
    
    def display_testimonial_count(self, obj):
       return str(obj.testimonials.count())

    display_testimonial_count.short_description = 'Testimonial'
    
    list_display = ['display_clients_count', 'display_services_count', 'display_testimonial_count', 'about_text', 'is_active']
    actions = ['make_active', 'make_inactive']

@admin.register(Client) 
class ClientAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="100"/>'.format(obj.logo.url))
    
    image_tag.short_description = 'Logo'
    
    list_display = ['name', 'image_tag',]


@admin.register(Service) 
class ServiceAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="100"/>'.format(obj.icon.url))
    
    image_tag.short_description = 'Icon'

    list_display = ['title', 'image_tag',]


@admin.register(Testimonial) 
class TestimonalAdmin(admin.ModelAdmin):
    def content_tag(self, obj):
        return format_html(obj.content)
    
    def image_tag(self, obj):
        return format_html('<img src="{}" height="100"/>'.format(obj.avatar.url))
    
    image_tag.short_description = 'Image'
    
    list_display = ['name', 'content_tag', 'image_tag', ]

