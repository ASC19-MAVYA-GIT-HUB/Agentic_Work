# Filename: utils/element_finder.py
# Description: Centralized locator utility with layered fallback strategy and explicit waits

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

logger = logging.getLogger(__name__)

class ElementFinder:
    """
    Centralized utility for finding elements with layered fallback strategy.
    Priority: accessibility selectors > data-testid > semantic selectors > visible text.
    """

    def __init__(self, driver, timeout=10, poll_frequency=0.5):
        self.driver = driver
        self.timeout = timeout
        self.poll_frequency = poll_frequency

    def find(self, element_name, page_name, locator_dict):
        current_url = self.driver.current_url
        for strategy, locator in locator_dict.items():
            if not locator:
                continue
            try:
                logger.info(f"[{page_name}] Trying {strategy} locator for '{element_name}' on {current_url}: {locator}")
                wait = WebDriverWait(self.driver, self.timeout, self.poll_frequency)
                element = wait.until(EC.presence_of_element_located(locator))
                logger.info(f"[{page_name}] Found '{element_name}' using {strategy} locator.")
                return element
            except (TimeoutException, NoSuchElementException):
                logger.debug(f"[{page_name}] '{element_name}' not found with {strategy} locator.")
                continue
        error_msg = f"Element '{element_name}' not found on page '{page_name}'. URL: {current_url}. Tried strategies: {list(locator_dict.keys())}"
        logger.error(error_msg)
        raise NoSuchElementException(error_msg)

    def find_clickable(self, element_name, page_name, locator_dict):
        current_url = self.driver.current_url
        for strategy, locator in locator_dict.items():
            if not locator:
                continue
            try:
                logger.info(f"[{page_name}] Trying {strategy} locator for clickable '{element_name}' on {current_url}: {locator}")
                wait = WebDriverWait(self.driver, self.timeout, self.poll_frequency)
                element = wait.until(EC.element_to_be_clickable(locator))
                logger.info(f"[{page_name}] Found clickable '{element_name}' using {strategy} locator.")
                return element
            except (TimeoutException, NoSuchElementException):
                logger.debug(f"[{page_name}] Clickable '{element_name}' not found with {strategy} locator.")
                continue
        error_msg = f"Clickable element '{element_name}' not found on page '{page_name}'. URL: {current_url}. Tried strategies: {list(locator_dict.keys())}"
        logger.error(error_msg)
        raise NoSuchElementException(error_msg)