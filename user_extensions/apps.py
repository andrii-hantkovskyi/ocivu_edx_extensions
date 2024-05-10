from django.apps import AppConfig

from openedx.core.djangoapps.plugins.constants import (
    ProjectType, SettingsType, PluginSettings
)


EXTENSIONS_APP_NAME = 'user_extensions'


class UserExtensionsConfig(AppConfig):
    """
    Open Civil University user extensions configuration.
    """
    name = EXTENSIONS_APP_NAME
    verbose_name = 'User Extensions'

    # Class attribute that configures and enables this app as a Plugin App.
    plugin_app = {
        PluginSettings.CONFIG: {
            ProjectType.CMS: {
                SettingsType.COMMON: {
                    PluginSettings.RELATIVE_PATH: 'settings.common',
                },
                SettingsType.DEVSTACK: {
                    PluginSettings.RELATIVE_PATH: 'settings.common',
                },
            },
            ProjectType.LMS: {
                SettingsType.COMMON: {
                    PluginSettings.RELATIVE_PATH: 'settings.common',
                },
                SettingsType.DEVSTACK: {
                    PluginSettings.RELATIVE_PATH: 'settings.common',
                },
            },
        }
    }