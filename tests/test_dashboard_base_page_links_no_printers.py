# Filename: tests/test_dashboard_base_page_links_no_printers.py
# Description: Refactored test using Page Object Model and centralized locators

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_provider import ConfigProvider
from pages.dashboard_page import DashboardPage
from utils.selenium_actions import click_element, assert_element_visible

@pytest.fixture
def driver():
    options = Options()
    if ConfigProvider().get('HEADLESS', 'true').lower() == 'true':
        options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def config():
    return ConfigProvider()

def test_dashboard_base_page_links_no_printers(driver, config):
    driver.get(config.base_url)
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    email_field.clear()
    email_field.send_keys(config.username)
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    password_field.clear()
    password_field.send_keys(config.password)
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    click_element(login_button, "Login Button", "Login", driver)

    dashboard = DashboardPage(driver)

    welcome_banner = dashboard.get_welcome_banner()
    assert_element_visible(welcome_banner, "Welcome Banner", "Dashboard", driver)

    install_hp_smart_app_btn = dashboard.get_install_hp_smart_app_button()
    assert_element_visible(install_hp_smart_app_btn, "Install HP Smart App Button", "Dashboard", driver)
    click_element(install_hp_smart_app_btn, "Install HP Smart App Button", "Dashboard", driver)
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    assert "app store" in driver.current_url.lower()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    download_now_link = dashboard.get_download_now_link()
    click_element(download_now_link, "Download Now Link", "Dashboard", driver)
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    assert "app store" in driver.current_url.lower()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    learn_more_link = dashboard.get_learn_more_link()
    click_element(learn_more_link, "Learn More Link", "Dashboard", driver)
    sustainability_page = dashboard.get_sustainability_page()
    assert_element_visible(sustainability_page, "Sustainability Page", "Dashboard", driver)