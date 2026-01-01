import os

class ConfigProvider:
    """
    Provides environment-specific configuration from environment variables.
    Falls back to defaults if not set, for backward compatibility.
    """
    @staticmethod
    def get_base_url():
        return os.environ.get("BASE_URL", "https://smb.pie.portalshell.int.hp.com")

    @staticmethod
    def get_stage_url():
        return os.environ.get("STAGE_URL", "https://smb.stage.portalshell.int.hp.com")

    @staticmethod
    def get_username():
        return os.environ.get("PORTAL_USERNAME", "")

    @staticmethod
    def get_password():
        return os.environ.get("PORTAL_PASSWORD", "")

    @staticmethod
    def get_wait_timeout():
        return int(os.environ.get("SELENIUM_EXPLICIT_WAIT", "10"))

    @staticmethod
    def get_wait_interval():
        return float(os.environ.get("SELENIUM_WAIT_INTERVAL", "0.5"))
