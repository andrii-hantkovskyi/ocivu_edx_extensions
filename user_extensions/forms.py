from django import forms
from .models import ExtendedUserProfile
from django.conf import settings
from django.utils.translation import gettext as _


class ExtendedUserProfileForm(forms.ModelForm):
    """
    Form that is used to extend registration form with additional
    fields taken from ExtendedUserProfile model
    """
    
    class Meta:
        model = ExtendedUserProfile
        fields = ('identity',)
        labels = {
            'identity': _('Country'),
        }
        help_texts = {
            'identity': _('Select an identity from the list'),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in settings.OCU_EXTENDED_PROFILE_FIELDS:
            self.fields[field_name].required = True