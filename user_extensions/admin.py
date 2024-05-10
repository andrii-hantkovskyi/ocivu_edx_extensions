
"""
Admin registration for user extensions.
"""


from django.contrib import admin

from .models import ExtendedUserProfile


@admin.register(ExtendedUserProfile)
class ExtendedUserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'identity'
    ]
    search_fields = ('identity',)