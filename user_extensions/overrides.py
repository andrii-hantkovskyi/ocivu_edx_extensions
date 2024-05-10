from django.conf import settings

from .models import ExtendedUserProfile


def do_create_account(base_fn, *args, **kwargs):
    """
    Override function do_create_account for adding in User object
    fields 'identity'

    Returns a tuple (User, UserProfile, Registration).
    """
    user, profile, registration = base_fn(*args, **kwargs)

    ExtendedUserProfile.objects.update_or_create(user=user, identity=registration.cleaned_data.get('identity'))
    extended_profile, _ = ExtendedUserProfile.objects.get_or_create(user=user)
    extended_profile.identity = registration.cleaned_data.get('identity')
    extended_profile.save()

    return user, profile, registration


def authn_field_can_be_saved(prev_fn, self, field):
    """
    Override _field_can_be_saved
    """
    return field in settings.OCU_EXTENDED_PROFILE_FIELDS or prev_fn(self, field)
