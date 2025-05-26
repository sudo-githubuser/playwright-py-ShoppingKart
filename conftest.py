import os
import platform
import shutil
import subprocess
from pathlib import Path
import allure
import pytest
from allure_commons.reporter import AllureReporter
from playwright.sync_api import Browser, Page, sync_playwright, expect
from helper.dataProvider.ConfigFileReader import ConfigFileReader
from helper.enums.DriverType import BrowserType
from helper.utility.DataGenerator import TestDataGenerator
from helper.utility.ExcelReader import ExcelFileManager
from helper.utility.JsonReader import JSONFileManager
from pageObjects.objectRepository.CreateAccount import CreateAccountPage

# Get project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
print(f"Conftest PROJECT_ROOT: {PROJECT_ROOT}")

# Create screenshots directory in project root/reports
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# Allure results and report directories in project root
ALLURE_RESULTS_DIR = os.path.join(REPORTS_DIR, "allure-results")
ALLURE_REPORT_DIR = os.path.join(REPORTS_DIR, "allure-report")
os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)
os.makedirs(ALLURE_REPORT_DIR, exist_ok=True)

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

@pytest.fixture(scope="session") # Remove scope='session' if you want to pass the data for each test (in parallel test)
def random_data():
    return TestDataGenerator().user_data

# Hook to generate Allure report after test session
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Generate Allure report after all tests are complete"""
    print("Generating Allure report...")

    # Locate allure executable
    allure_cmd = shutil.which("allure")
    if not allure_cmd:
        # Fallback to common Allure installation paths
        common_paths = [
            os.path.join(os.environ.get("PROGRAMFILES", "C:/Program Files"), "allure/bin/allure.bat"),  # Windows
            os.path.join(os.environ.get("USERPROFILE", "C:/Users/"), "allure/bin/allure.bat"),  # Windows
            os.path.join(os.environ.get("USERPROFILE", "C:/Users/"), "allure-2.30.0/bin/allure.bat"), # Windows
            os.path.join(os.environ.get("NODEJS_PATH", "C:/nvm4w/nodejs"), "allure.bat")
        ]
        for path in common_paths:
            if os.path.exists(path):
                allure_cmd = path
                break

    if not allure_cmd:
        print("Allure CLI not found. Please install Allure and ensure it's in your PATH.")
        print("Installation instructions: https://docs.qameta.io/allure/#_installing_a_commandline")
        return

    # Clean report directory
    if os.path.exists(ALLURE_REPORT_DIR):
        try:
            shutil.rmtree(ALLURE_REPORT_DIR)
        except Exception as e:
            print(f"Failed to clean allure-report directory: {e}")

    try:
        result = subprocess.run(
            [allure_cmd, "generate", ALLURE_RESULTS_DIR, "--clean", "-o", ALLURE_REPORT_DIR],
            check=True,
            capture_output=True,
            text=True,
            shell=(platform.system() == "Windows")  # Use shell=True on Windows for .bat files
        )
        print(f"Allure report generated at {ALLURE_REPORT_DIR}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate Allure report: {e.stderr}")
    except FileNotFoundError as e:
        print(f"Allure command not found at {allure_cmd}: {e}")


@pytest.fixture
def create_account(page):
    """Provides CreateAccountPage instance"""
    return CreateAccountPage(page)