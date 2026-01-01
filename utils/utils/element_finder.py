import logging
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

logger = logging.getLogger(__name__)

class ElementFinder:
    """
    Utility to find elements using a layered fallback strategy:
    1. accessibility selectors (aria-label, role)
    2. data-testid attributes
    3. semantic selectors (e.g., role, type)
    4. visible text (as last resort)
    """
    def __init__(self, driver, timeout=None, poll_frequency=None):
        self.driver = driver
        self.timeout = timeout or int(os.environ.get("SELENIUM_EXPLICIT_WAIT", "10"))
        self.poll_frequency = poll_frequency or float(os.environ.get("SELENIUM_WAIT_INTERVAL", "0.5"))

    def find(self, element_name, page_name, locator_dict):
        """
        Try to locate an element using the provided locator strategies in order.
        locator_dict: Ordered dict or list of (by, value) tuples in priority order.
        """
        current_url = self.driver.current_url
        for strategy in locator_dict:
            by, value, label = strategy
            try:
                wait = WebDriverWait(self.driver, self.timeout, self.poll_frequency)
                element = wait.until(EC.presence_of_element_located((by, value)))
                logger.info(f"[{page_name}] Found '{element_name}' using {label} ({by}, {value}) on {current_url}")
                return element
            except (TimeoutException, NoSuchElementException):
                logger.debug(f"[{page_name}] Could not find '{element_name}' using {label} ({by}, {value}) on {current_url}")
                continue
        error_msg = f"[{page_name}] Failed to find '{element_name}' on page {current_url} using any locator strategy"
        logger.error(error_msg)
        raise NoSuchElementException(error_msg)

    def click(self, element, element_name, page_name):
        try:
            element.click()
            logger.info(f"[{page_name}] Clicked on '{element_name}' at {self.driver.current_url}")
        except Exception as e:
            logger.error(f"[{page_name}] Error clicking '{element_name}' at {self.driver.current_url}: {str(e)}")
            raise

    def assert_visible(self, element, element_name, page_name):
        try:
            assert element.is_displayed(), f"Element '{element_name}' not visible on {page_name} ({self.driver.current_url})"
            logger.info(f"[{page_name}] '{element_name}' is visible at {self.driver.current_url}")
        except AssertionError as e:
            logger.error(str(e))
            raise

# Helper to build locator strategies in priority order
def build_locator_strategy(element_labels):
    """
    element_labels: dict with possible keys: aria_label, data_testid, role, text
    Returns: list of (By, value, label) tuples in priority order.
    """
    strategies = []
    if "aria_label" in element_labels:
        strategies.append((By.CSS_SELECTOR, f"[aria-label='{element_labels['aria_label']}']", "aria-label"))
    if "data_testid" in element_labels:
        strategies.append((By.CSS_SELECTOR, f"[data-testid='{element_labels['data_testid']}']", "data-testid"))
    if "role" in element_labels:
        strategies.append((By.CSS_SELECTOR, f"[role='{element_labels['role']}']", "role"))
    if "text" in element_labels:
        # Only as last resort, prefer CSS selectors
        strategies.append((By.XPATH, f"//*[normalize-space(text())='{element_labels['text']}']", "visible text"))
    return strategies
