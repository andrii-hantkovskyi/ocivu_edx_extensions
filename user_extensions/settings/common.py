"""
Common Django settings for user_extensions app.
"""


# pylint: disable=unnecessary-pass,unused-argument
def plugin_settings(settings):
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """

    settings.OVERRIDE_DO_CREATE_ACCOUNT = 'user_extensions.overrides.do_create_account'

    if settings.FEATURES.get("ENABLE_OCU_EXTENDED_REG_FORM", True):
        settings.REGISTRATION_EXTENSION_FORM = 'user_extensions.forms.ExtendedUserProfileForm'
        settings.OCU_EXTENDED_PROFILE_FIELDS = ['identity']
        settings.OCU_EXTENDED_PROFILE_EXTRA_FIELDS = {
            'identity': 'required',
        }
        settings.REGISTRATION_EXTRA_FIELDS.update(settings.OCU_EXTENDED_PROFILE_EXTRA_FIELDS)
        settings.REGISTRATION_FIELD_ORDER += settings.OCU_EXTENDED_PROFILE_FIELDS

        settings.OVERRIDE_OCU_PROFILE_FIELDS = "user_extensions.overrides.authn_field_can_be_saved"