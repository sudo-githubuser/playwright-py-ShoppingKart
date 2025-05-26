import os
from datetime import datetime

import allure
from pytest_bdd import scenario, given, when, then

SCREENSHOTS_DIR = os.path.join(os.getcwd(), "screenshots")

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
    attach_screenshot(page, "user_is_on_the_home_page",
                      "create_an_account_with_valid_and_unique_email_id")
    return page

@when('User navigates to create account page')
@allure.step("Navigate to create account page")
def navigate_to_create_account_page(page, create_account):
    """Click the 'Create an Account' link"""
    create_account.navigate_to_create_account()
    attach_screenshot(page, "user_navigates_to_create_account_page",
                      "create_an_account_with_valid_and_unique_email_id")


@when('User fills the registration form with valid data')
@allure.step("Fill registration form with valid data")
def enter_user_details(page, create_account, random_data):
    """Enter valid user details from random_data"""
    create_account.fill_form(first_name=random_data["first name"],
                             last_name=random_data["last name"],
                             email=random_data["email"],
                             password=random_data["password"]
                             )
    attach_screenshot(page, "user_fills_the_registration_form_with_valid_data",
                      "create_an_account_with_valid_and_unique_email_id")

@when('User submits the form')
@allure.step("Submit the registration form")
def submit_form(page, create_account):
    """Submit the account creation form"""
    create_account.submit_form()
    attach_screenshot(page, "user_submits_the_form",
                      "create_an_account_with_valid_and_unique_email_id")

@then('User should see the account creation success message')
@allure.step("Verify account creation success message")
def verify_success_message(page, create_account):
    """Verify the account creation success message"""
    create_account.expect_success_message()
    attach_screenshot(page, "user_should_see_the_account_creation_success_message",
                      "create_an_account_with_valid_and_unique_email_id")

