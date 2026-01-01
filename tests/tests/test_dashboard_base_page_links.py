import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_provider import ConfigProvider
from pages.dashboard_page import DashboardPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # For CI/CD readiness
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_dashboard_base_page_links_no_printers(driver):
    config = ConfigProvider()
    dashboard_url = config.get_base_url()
    driver.get(dashboard_url)
    dashboard = DashboardPage(driver)

    # Step 1: Welcome Banner
    welcome_banner = dashboard.get_welcome_banner()
    dashboard.finder.assert_visible(welcome_banner, "Welcome Banner", "Dashboard")

    # Step 1: Install HP Smart App button
    install_btn = dashboard.get_install_hp_smart_app_btn()
    dashboard.finder.assert_visible(install_btn, "Install HP Smart App Button", "Dashboard")

    # Step 1: Get HP app card
    get_hp_app_card = dashboard.get_download_now_link()
    dashboard.finder.assert_visible(get_hp_app_card, "Download Now Link", "Dashboard")

    # Step 1: Sustainability card
    sustainability_card = dashboard.get_sustainability_card()
    dashboard.finder.assert_visible(sustainability_card, "Sustainability Card", "Dashboard")

    # Step 2: Click 'Install HP Smart App' button and verify redirection
    dashboard.finder.click(install_btn, "Install HP Smart App Button", "Dashboard")
    try:
        WebDriverWait(driver, config.get_wait_timeout()).until(
            lambda d: "appstore" in d.current_url or "store" in d.current_url
        )
    except TimeoutException:
        pytest.fail(f"Redirection to app store failed after clicking 'Install HP Smart App' on {driver.current_url}")

    # Step 3: Click 'Download now' link and verify redirection
    driver.get(dashboard_url)
    download_now_link = dashboard.get_download_now_link()
    dashboard.finder.click(download_now_link, "Download Now Link", "Dashboard")
    try:
        WebDriverWait(driver, config.get_wait_timeout()).until(
            lambda d: "appstore" in d.current_url or "store" in d.current_url
        )
    except TimeoutException:
        pytest.fail(f"Redirection to app store failed after clicking 'Download Now' on {driver.current_url}")

    # Step 4: Click 'Learn more' link and verify Sustainability page
    driver.get(dashboard_url)
    learn_more_link = dashboard.get_learn_more_link()
    dashboard.finder.click(learn_more_link, "Learn More Link", "Dashboard")
    try:
        WebDriverWait(driver, config.get_wait_timeout()).until(
            lambda d: "sustainability" in d.current_url.lower() or "sustainability" in d.title.lower()
        )
    except TimeoutException:
        pytest.fail(f"Redirection to Sustainability page failed after clicking 'Learn More' on {driver.current_url}")
