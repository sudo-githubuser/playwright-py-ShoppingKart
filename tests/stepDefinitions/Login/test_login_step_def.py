import os
from datetime import datetime
from pathlib import Path

import allure
from pytest_bdd import scenario, given, when, then

from helper.utility.JsonReader import JSONFileManager

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
print(f"StepDef PROJECT_ROOT: {PROJECT_ROOT}")
SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT, "reports", "screenshots")

@allure.epic("User Account")
@allure.feature("Login")
@allure.story("Login with valid email ID")
@scenario('../features/Login.feature', 'Login with valid user credentials')
def test_login():
    """Test login scenario"""
    pass

def attach_screenshot(page, step_name, scenario_name):
    """Helper function to capture and attach screenshot"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    step_name = step_name.replace(" ", "_").lower()
    scenario_name = scenario_name.replace(" ", "_").lower()
    screenshot_name = f"{scenario_name}_{step_name}_{timestamp}.png"
    screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)

    try:
        page.screenshot(path=screenshot_path, full_page=True)
        with open(screenshot_path, "rb") as image_file:
            allure.attach(
                body=image_file.read(),
                name=screenshot_name,
                attachment_type=allure.attachment_type.PNG
            )
        print(f"Screenshot saved: {screenshot_path}")
    except Exception as e:
        print(f"Failed to capture screenshot for {step_name}: {e}")

@given('User is on the home page')
@allure.step("Navigate to the home page")
def user_in_home_page(page):
    """Ensure user is on the home page (handled by page fixture)"""
    # Page is already navigated to base_url by conftest.py
    attach_screenshot(page, "User is on the home page",
                      "Login with valid email ID and password")
    return page

@when('User navigates to login page')
@allure.step("Navigate to login page")
def navigate_to_login_page(page, login):
    """Click the 'Create an Account' link"""
    login.navigate_to_login_page()
    login.expect_login_page_message()
    attach_screenshot(page, "User navigates to login page",
                      "Login with valid email ID and password")

@given('User enters valid email address, password')
@allure.step('Enter valid email ID and password')
def enter_valid_email_address(page, login, random_data):
    json_manager = JSONFileManager()
    credentials = json_manager.get_credentials()
    login.enter_credentials(credentials["email"], credentials["password"])
    attach_screenshot(page, "User enters valid email address, password",
                      "Login with valid email ID and password")

@when('User clicks on sign in')
@allure.step('Click on Sign In button')
def sign_in(page, login):
    login.user_login()
    attach_screenshot(page, "User clicks on sign in",
                      "Login with valid email ID and password")

@then('Home page is displayed')
@allure.step('User logged in successfully')
def verify_sign_in(page, login):
    login.expect_home_page_message()
    attach_screenshot(page, "Home page is displayed",
                      "Login with valid email ID and password")

@then('User is logged out')
def user_logout(page, login):
    login.user_logout()
    attach_screenshot(page, "User logged out",
                      "Login with valid email ID and password")



