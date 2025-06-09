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
@allure.feature("Registration")
@allure.story("Create Account")
@scenario('../features/CreateAccount.feature', 'Create an account with valid and unique email ID')
def test_create_account():
    """Test create account scenario"""
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
                      "Create an account with valid and unique email id")
    return page

@when('User navigates to create account page')
@allure.step("Navigate to create account page")
def navigate_to_create_account_page(page, create_account):
    """Click the 'Create an Account' link"""
    create_account.navigate_to_create_account()
    attach_screenshot(page, "User navigates to create account page",
                      "Create an account with valid and unique email id")


@when('User fills the registration form with valid data')
@allure.step("Fill registration form with valid data")
def enter_user_details(page, create_account, random_data):
    """Enter valid user details from random_data"""
    create_account.fill_form(first_name=random_data["first name"],
                             last_name=random_data["last name"],
                             email=random_data["email"],
                             password=random_data["password"]
                             )
    attach_screenshot(page, "User fills the registration form with valid data",
                      "Create an account with valid and unique email id")

@when('User submits the form')
@allure.step("Submit the registration form")
def submit_form(page, create_account, random_data):
    """Submit the account creation form"""
    create_account.submit_form()
    # Save email and password to JSON if empty
    json_manager = JSONFileManager()
    json_manager.save_credentials_if_empty(
        first_name = random_data['first name'],
        last_name = random_data['last name'],
        email = random_data["email"],
        password = random_data["password"]
    )
    attach_screenshot(page, "User submits the form",
                      "Create an account with valid and unique email id")

@then('User should see the account creation success message')
@allure.step("Verify account creation success message")
def verify_success_message(page, create_account):
    """Verify the account creation success message"""
    create_account.expect_success_message()
    attach_screenshot(page, "User should see the account creation success message",
                      "Create an account with valid and unique email id")

