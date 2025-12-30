# Filename: utils/config_provider.py
# Description: Secure configuration provider abstraction using environment variables

import os

class ConfigProvider:
    """
    Abstraction for environment-specific configuration.
    Reads from environment variables, with optional defaults for backward compatibility.
    """
    @staticmethod
    def get(key, default=None):
        return os.environ.get(key, default)

    @property
    def base_url(self):
        return self.get('BASE_URL')

    @property
    def username(self):
        return self.get('USERNAME')

    @property
    def password(self):
        return self.get('PASSWORD')