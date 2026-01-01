# Filename: pages/dashboard_page.py
# Description: Page Object Model for Dashboard, using ElementFinder for robust locator strategy and error handling.

from utils.element_finder import ElementFinder, build_locator_strategy

class DashboardPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.finder = ElementFinder(driver, timeout=timeout)

    def assert_welcome_banner(self):
        locator_dict = build_locator_strategy({
            "locator_type": "aria-label",
            "locator_value": "Welcome Banner"
        })
        self.finder.assert_visible("Welcome Banner", locator_dict, page_context="Dashboard")

    def click_install_hp_smart_app(self):
        locator_dict = build_locator_strategy({
            "locator_type": "data-testid",
            "locator_value": "install-hp-smart-app-btn"
        })
        self.finder.click("Install HP Smart App Button", locator_dict, page_context="Dashboard")

    def click_download_now(self):
        locator_dict = build_locator_strategy({
            "locator_type": "aria-label",
            "locator_value": "Download Now"
        })
        self.finder.click("Download Now Link", locator_dict, page_context="Dashboard")

    def click_learn_more(self):
        locator_dict = build_locator_strategy({
            "locator_type": "aria-label",
            "locator_value": "Learn More"
        })
        self.finder.click("Learn More Link", locator_dict, page_context="Dashboard")

    def assert_sustainability_card(self):
        locator_dict = build_locator_strategy({
            "locator_type": "aria-label",
            "locator_value": "Sustainability"
        })
        self.finder.assert_visible("Sustainability Card", locator_dict, page_context="Dashboard")

    # Add additional methods for other critical elements as needed
