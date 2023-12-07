from django.contrib import admin
from mixins.active import ActivateDeactivateMixin

from .models import Account, Contact, Social

class AccountAdmin(ActivateDeactivateMixin, admin.ModelAdmin):
    list_display = ('name', 'title', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('name', 'title',)
    actions = ['make_active', 'make_inactive']

# Register your model
admin.site.register(Account, AccountAdmin)
admin.site.register(Contact)
admin.site.register(Social)