class ActivateDeactivateMixin:
    def make_active(self, request, queryset):
        if queryset.count() == 1:  # Only allow activation if a single object is selected
            # Ensure only one object is active at a time
            queryset.update(is_active=True)
            # Deactivate all other objects
            self.model.objects.exclude(pk__in=queryset.values_list('pk', flat=True)).update(is_active=False)
        else:
            self.message_user(request, "Please select only one object to activate.", level='error')

    make_active.allowed_permissions = ('change',)  # Add the 'change' permission check
    make_active.action_present = "Make Active"  # Customize the action label
    make_active.short_description = "Make Active"  # Customize the tooltip

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = "Make Inactive"  # Customize the tooltip