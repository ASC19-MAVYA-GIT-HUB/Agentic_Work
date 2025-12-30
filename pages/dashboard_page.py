# Filename: pages/dashboard_page.py
# Description: Page Object Model for Dashboard, using centralized locator utility and improved error handling

from selenium.webdriver.common.by import By
from utils.element_finder import ElementFinder
from utils.selenium_actions import click_element, assert_element_visible

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.element_finder = ElementFinder(driver)

    def get_welcome_banner(self):
        locators = {
            'accessibility': (By.XPATH, "//*[@aria-label='Welcome Banner']"),
            'data-testid': (By.CSS_SELECTOR, "[data-testid='welcome-banner']"),
            'semantic': (By.CSS_SELECTOR, "section.welcome-banner"),
            'text': (By.XPATH, "//*[text()='Welcome Banner']")
        }
        return self.element_finder.find("Welcome Banner", "Dashboard", locators)

    def get_install_hp_smart_app_button(self):
        locators = {
            'accessibility': (By.XPATH, "//*[@aria-label='Install HP Smart App']"),
            'data-testid': (By.CSS_SELECTOR, "[data-testid='install-hp-smart-app']"),
            'semantic': (By.CSS_SELECTOR, "button.install-hp-smart-app"),
            'text': (By.XPATH, "//button[text()='Install HP Smart App']")
        }
        return self.element_finder.find_clickable("Install HP Smart App Button", "Dashboard", locators)

    def get_download_now_link(self):
        locators = {
            'accessibility': (By.XPATH, "//*[@aria-label='Download now']"),
            'data-testid': (By.CSS_SELECTOR, "[data-testid='download-now']"),
            'semantic': (By.CSS_SELECTOR, "a.download-now"),
            'text': (By.XPATH, "//a[text()='Download now']")
        }
        return self.element_finder.find_clickable("Download Now Link", "Dashboard", locators)

    def get_learn_more_link(self):
        locators = {
            'accessibility': (By.XPATH, "//*[@aria-label='Learn more']"),
            'data-testid': (By.CSS_SELECTOR, "[data-testid='learn-more']"),
            'semantic': (By.CSS_SELECTOR, "a.learn-more"),
            'text': (By.XPATH, "//a[text()='Learn more']")
        }
        return self.element_finder.find_clickable("Learn More Link", "Dashboard", locators)

    def get_sustainability_page(self):
        locators = {
            'accessibility': (By.XPATH, "//*[@aria-label='Sustainability page']"),
            'data-testid': (By.CSS_SELECTOR, "[data-testid='sustainability-page']"),
            'semantic': (By.CSS_SELECTOR, "section.sustainability-page"),
            'text': (By.XPATH, "//*[text()='Sustainability']")
        }
        return self.element_finder.find("Sustainability Page", "Dashboard", locators)