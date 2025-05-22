import pytest
from playwright.sync_api import Browser, Page, sync_playwright
from helper.dataProvider.ConfigFileReader import ConfigFileReader
from helper.enums.DriverType import BrowserType
from helper.utility.DataGenerator import TestDataGenerator
from helper.utility.ExcelReader import ExcelFileManager
from helper.utility.JsonReader import JSONFileManager


@pytest.fixture(scope='session')
def config():
    return ConfigFileReader()

@pytest.fixture(scope='session')
def browser_type(config):
    return config.get_browser()

@pytest.fixture(scope="session")
def headless(config):
    return config.is_headless()

@pytest.fixture(scope='session')
def base_url(config):
    return config.get_application_url()

@pytest.fixture(scope="session")
def browser(browser_type: BrowserType, headless: bool):
    with sync_playwright() as p:
        if browser_type == BrowserType.CHROME:
            browser = p.chromium.launch(channel="chrome", headless=headless)
        elif browser_type == BrowserType.FIREFOX:
            browser = p.firefox.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser: {browser_type}")
        try:
            yield browser
        finally:
            browser.close()

@pytest.fixture(scope='session')
def page(browser, base_url: str):
    page = browser.new_page()
    try:
        page.goto(base_url)
        yield page
    finally:
        page.close()

@pytest.fixture(scope="session")
def read_value_json():
    return JSONFileManager().read()

@pytest.fixture(scope="session")
def read_value_excel():
    return ExcelFileManager().read_excel_data()

@pytest.fixture(scope="session") # Remove scope=session if you want to pass the data for each test (in parallel test)
def random_data():
    return TestDataGenerator().user_data