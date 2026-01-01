# Filename: conftest.py
# Description: Centralized Pytest fixture for driver and config, ensuring test isolation and compatibility with existing test execution.

import pytest
from selenium import webdriver
from config.config_provider import ConfigProvider

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config():
    return ConfigProvider()
