# Filename: utils/element_finder.py
# Description: Centralized locator utility implementing layered fallback strategy (accessibility, data-testid, semantic, visible text) with explicit waits, configurable timeout, and POM integration.

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

logger = logging.getLogger(__name__)

class ElementFinder:
    """
    Centralized locator utility for robust element finding with layered fallback.
    Priority: accessibility (aria-label/role), data-testid, semantic selectors, visible text (last resort).
    """

    def __init__(self, driver, timeout=10, poll_frequency=0.5):
        self.driver = driver
        self.timeout = timeout
        self.poll_frequency = poll_frequency

    def find(self, element_name, locator_dict, page_context=None):
        """
        Attempts to find an element using locator strategies in order.
        Args:
            element_name: str, logical name for logging
            locator_dict: Ordered dict/list of (by, value) tuples in priority order
            page_context: str, page/component context for diagnostics
        Returns:
            WebElement if found
        Raises:
            NoSuchElementException with detailed error message
        """
        current_url = self.driver.current_url
        context = f"Page: {page_context or 'Unknown'} | Element: {element_name} | URL: {current_url}"
        logger.info(f"Finding element: {element_name} ({context})")
        for by, value, strategy in locator_dict:
            try:
                wait = WebDriverWait(self.driver, self.timeout, self.poll_frequency)
                element = wait.until(EC.presence_of_element_located((by, value)))
                logger.debug(f"Found '{element_name}' using {strategy} ({by}, {value})")
                return element
            except (TimeoutException, NoSuchElementException):
                logger.debug(f"Not found with {strategy} ({by}, {value})")
                continue
        error_msg = f"[ERROR] Could not locate '{element_name}' using any strategy. {context}"
        logger.error(error_msg)
        raise NoSuchElementException(error_msg)

    def click(self, element_name, locator_dict, page_context=None):
        """
        Waits for element to be clickable and clicks it, with error handling and logging.
        """
        element = self.find(element_name, locator_dict, page_context)
        try:
            wait = WebDriverWait(self.driver, self.timeout, self.poll_frequency)
            clickable = wait.until(EC.element_to_be_clickable((element.by, element.value)))
            logger.info(f"Clicking '{element_name}' on {page_context or 'Unknown'}")
            clickable.click()
        except Exception as e:
            error_msg = f"[ERROR] Failed to click '{element_name}' on {page_context or 'Unknown'} | URL: {self.driver.current_url} | Exception: {e}"
            logger.error(error_msg)
            raise

    def assert_visible(self, element_name, locator_dict, page_context=None):
        """
        Asserts that an element is visible, with error handling and logging.
        """
        try:
            wait = WebDriverWait(self.driver, self.timeout, self.poll_frequency)
            element = self.find(element_name, locator_dict, page_context)
            visible = wait.until(EC.visibility_of(element))
            assert visible.is_displayed(), f"{element_name} not visible on {page_context}"
            logger.info(f"Asserted visible: '{element_name}' on {page_context or 'Unknown'}")
        except Exception as e:
            error_msg = f"[ERROR] Visibility assertion failed for '{element_name}' on {page_context or 'Unknown'} | URL: {self.driver.current_url} | Exception: {e}"
            logger.error(error_msg)
            raise

# Helper to build locator strategies in order of priority
def build_locator_strategy(locator_info):
    """
    Accepts a locator_info dict with keys: locator_type, locator_value.
    Returns a prioritized list of (By, value, strategy_name) tuples.
    """
    strategies = []
    if locator_info.get("locator_type") == "aria-label":
        strategies.append((By.CSS_SELECTOR, f'[aria-label="{locator_info["locator_value"]}"]', "aria-label"))
    if locator_info.get("locator_type") == "data-testid":
        strategies.append((By.CSS_SELECTOR, f'[data-testid="{locator_info["locator_value"]}"]', "data-testid"))
    if locator_info.get("locator_type") == "role+name":
        # Example: "button[Manage Printer]" means role=button, name=Manage Printer
        role, name = locator_info["locator_value"].split("[", 1)
        name = name.rstrip("]")
        strategies.append((By.XPATH, f'//*[@role="{role}" and normalize-space()="{name}"]', "role+name"))
    # As a last resort, try visible text (brittle, but fallback)
    strategies.append((By.XPATH, f'//*[contains(text(), "{locator_info["locator_value"]}")]', "visible text"))
    return strategies
