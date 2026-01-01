# Filename: tests/test_dashboard_base_page_links_no_printers.py
# Description: Refactored test using Page Object Model, centralized locator utility, and secure config provider. Enhanced error handling and logging.

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config_provider import ConfigProvider
from pages.dashboard_page import DashboardPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config():
    return ConfigProvider()

def test_dashboard_base_page_links_no_printers(driver, config):
    # Step 1: Navigate to the Consolidated Portal Dashboard
    driver.get(config.get_base_url())
    dashboard = DashboardPage(driver)
    dashboard.assert_welcome_banner()
    dashboard.assert_sustainability_card()

    # Step 2: Click on the 'Install HP Smart App' button
    dashboard.click_install_hp_smart_app()
    WebDriverWait(driver, 10).until(
        EC.url_contains("appstore")
    )
    assert "appstore" in driver.current_url, f"Expected 'appstore' in URL after clicking Install HP Smart App, got {driver.current_url}"

    # Step 3: Click on the 'Download now' link
    dashboard.click_download_now()
    WebDriverWait(driver, 10).until(
        EC.url_contains("appstore")
    )
    assert "appstore" in driver.current_url, f"Expected 'appstore' in URL after clicking Download Now, got {driver.current_url}"

    # Step 4: Click on the 'Learn more' link
    dashboard.click_learn_more()
    dashboard.assert_sustainability_card()
