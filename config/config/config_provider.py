# Filename: config/config_provider.py
# Description: Secure configuration provider abstraction using environment variables for URLs and credentials.

import os

class ConfigProvider:
    """
    Provides environment-specific configuration from environment variables.
    Falls back to defaults if not set, for backward compatibility.
    """
    def __init__(self):
        self.base_url = os.environ.get("BASE_URL", "https://smb.pie.portalshell.int.hp.com")
        self.stage_url = os.environ.get("STAGE_URL", "https://smb.stage.portalshell.int.hp.com")
        self.username = os.environ.get("PORTAL_USERNAME", "")
        self.password = os.environ.get("PORTAL_PASSWORD", "")

    def get_base_url(self):
        return self.base_url

    def get_stage_url(self):
        return self.stage_url

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
