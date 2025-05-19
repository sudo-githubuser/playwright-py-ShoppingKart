import pytest
from playwright.sync_api import Browser, Page
from helper.dataProvider.ConfigFileReader import ConfigFileReader

@pytest.fixture(scope='session')
def config():
    return ConfigFileReader()

@pytest.fixture()
def browser_type(config):
    return config.get_browser()

@pytest.fixture()
def base_url(config):
    return config.get_application_url()

@pytest.fixture()
def page(browser: Browser, base_url: str):
    page = browser.new_page()
    page.goto(base_url)
    yield page
    page.close()