# Filename: utils/selenium_actions.py
# Description: Lightweight logging wrappers and error handling for Selenium actions

import logging
from selenium.common.exceptions import WebDriverException

logger = logging.getLogger(__name__)

def click_element(element, element_name, page_name, driver):
    current_url = driver.current_url
    try:
        logger.info(f"[{page_name}] Attempting to click '{element_name}' on {current_url}")
        element.click()
        logger.info(f"[{page_name}] Clicked '{element_name}' on {current_url}")
    except WebDriverException as e:
        error_msg = f"Error clicking '{element_name}' on page '{page_name}'. URL: {current_url}. Exception: {e}"
        logger.error(error_msg)
        raise

def assert_element_visible(element, element_name, page_name, driver):
    current_url = driver.current_url
    try:
        assert element.is_displayed(), f"Element '{element_name}' not visible on page '{page_name}' ({current_url})"
        logger.info(f"[{page_name}] Verified visibility of '{element_name}' on {current_url}")
    except AssertionError as e:
        error_msg = f"Visibility assertion failed for '{element_name}' on page '{page_name}'. URL: {current_url}. Exception: {e}"
        logger.error(error_msg)
        raise