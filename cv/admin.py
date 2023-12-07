from django.contrib import admin

from mixins.active import ActivateDeactivateMixin
from .models import Cv, Skill, Experience, Education

class AccountAdmin(ActivateDeactivateMixin, admin.ModelAdmin):
    list_display = ('title', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
    actions = ['make_active', 'make_inactive']

# Register your model
admin.site.register(Cv, AccountAdmin)

admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)