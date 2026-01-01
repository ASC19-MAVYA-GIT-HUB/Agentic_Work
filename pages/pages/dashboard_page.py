from utils.element_finder import ElementFinder, build_locator_strategy

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.finder = ElementFinder(driver)

    def get_welcome_banner(self):
        locators = build_locator_strategy({"aria_label": "Welcome Banner"})
        return self.finder.find("Welcome Banner", "Dashboard", locators)

    def get_install_hp_smart_app_btn(self):
        locators = build_locator_strategy({
            "aria_label": "Install HP Smart App",
            "data_testid": "install-hp-smart-app-btn"
        })
        return self.finder.find("Install HP Smart App Button", "Dashboard", locators)

    def get_download_now_link(self):
        locators = build_locator_strategy({
            "aria_label": "Download now",
            "data_testid": "download-now-link"
        })
        return self.finder.find("Download Now Link", "Dashboard", locators)

    def get_learn_more_link(self):
        locators = build_locator_strategy({
            "aria_label": "Learn more",
            "data_testid": "learn-more-link"
        })
        return self.finder.find("Learn More Link", "Dashboard", locators)

    def get_sustainability_card(self):
        locators = build_locator_strategy({
            "aria_label": "Sustainability card",
            "data_testid": "sustainability-card"
        })
        return self.finder.find("Sustainability Card", "Dashboard", locators)
