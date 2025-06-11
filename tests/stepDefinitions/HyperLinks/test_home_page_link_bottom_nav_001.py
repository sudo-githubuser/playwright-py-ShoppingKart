import os
from datetime import datetime
from pathlib import Path

import allure
from pytest_bdd import scenario, given, when, then

from helper.utility.ScreenshotUtils import capture_and_attach_screenshot

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
print(f"StepDef PROJECT_ROOT: {PROJECT_ROOT}")
SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT, "reports", "screenshots")

@allure.epic("User Account")
@allure.feature("Registration")
@allure.story("Create Account")
@scenario('../features/HomePageLinks.feature', 'Homepage hyperlinks in bottom navigation bar-01')
def test_homepage_hyperlink():
    pass

@given('Home page is displayed')
@allure.step("Navigate to homepage")
def home_page_displayed(page):
    """Ensure user is on the home page (handled by page fixture)"""
    # Page is already navigated to base_url by conftest.py
    capture_and_attach_screenshot(
        page=page,
        step_name="User is on the home page"
    )
    return page

@when('User clicks on "Notes" link')
@allure.step("Navigate to Notes link")
def click_notes(homepage_hyperlink, page):
    """Click on a Notes link and capture homepage screenshot"""
    homepage_hyperlink.notes_verify()
    capture_and_attach_screenshot(
        page=page,
        step_name="Navigate to Notes link"
    )

@then('Notes page is displayed in new tab')
@allure.step("Verify Notes page in new tab")
def verify_notes_page():
    """Verify Notes page (assertion handled in HomePageHyperLink.notes)"""
    try:
        pass  # Assertion handled in HomePageHyperLink.notes
    except Exception as e:
        print(f"Failed to verify Notes page: {e}")
        allure.attach(
            body=str(e).encode(),
            name=f"verify_notes_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            attachment_type=allure.attachment_type.TEXT
        )

@when('User clicks on "Write for us" link')
@allure.step("Click Write for us link")
def click_write_for_us(homepage_hyperlink, page):
    """Click Write for us link and capture screenshot"""
    homepage_hyperlink.write_for_us_verify()
    capture_and_attach_screenshot(
        page=page,
        step_name="Navigate to Write for us link"
    )

@then('Write for us page is displayed in new tab')
@allure.step("Verify Write for us page in new tab")
def verify_write_for_us_page():
    """Verify Write for us page (assertion handled in HomePageHyperLink.write_for_us)"""
    try:
        pass  # Assertion handled in HomePageHyperLink.write_for_us
    except Exception as e:
        print(f"Failed to verify Write for us page: {e}")
        allure.attach(
            body=str(e).encode(),
            name=f"verify_write_for_us_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            attachment_type=allure.attachment_type.TEXT
        )

@when('User clicks on "Subscribe" link')
@allure.step("Click Subscribe link")
def click_subscribe(homepage_hyperlink, page):
    """Click Subscribe link and capture screenshot"""
    homepage_hyperlink.subscribe_verify()
    capture_and_attach_screenshot(
        page=page,
        step_name="Navigate to Subscribe link"
    )

@then('Subscribe page is displayed in new tab')
@allure.step("Verify Subscribe page in new tab")
def verify_subscribe_page():
    """Verify Subscribe page (assertion handled in HomePageHyperLink.subscribe)"""
    try:
        pass  # Assertion handled in HomePageHyperLink.subscribe
    except Exception as e:
        print(f"Failed to verify Subscribe page: {e}")
        allure.attach(
            body=str(e).encode(),
            name=f"verify_subscribe_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            attachment_type=allure.attachment_type.TEXT
        )

