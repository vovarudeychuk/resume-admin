from django.contrib import admin
from django.utils.html import format_html

from .models import About, Client, Service, Testimonial

# admin.site.register(About)
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    
    def display_clients_count(self, obj):
       return str(obj.clients.count())

    display_clients_count.short_description = 'Clients'
    
    def display_services_count(self, obj):
       return str(obj.services.count())

    display_services_count.short_description = 'Services'
    
    list_display = ['display_clients_count', 'display_services_count', 'about_text']

@admin.register(Client) 
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo',]


@admin.register(Service) 
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon',]


@admin.register(Testimonial) 
class TestimonalAdmin(admin.ModelAdmin):
    
    def content_tag(self, obj):
        return format_html(obj.content)
    

    def image_tag(self, obj):
        return format_html('<img src="{}" height="100"/>'.format(obj.avatar.url))
    

    image_tag.short_description = 'Image'
    
    list_display = ['name', 'content_tag', 'image_tag', ]



# Register your models here.
