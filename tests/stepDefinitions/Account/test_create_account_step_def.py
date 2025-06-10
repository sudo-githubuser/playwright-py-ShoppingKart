import allure
from pytest_bdd import scenario, given, when, then
from helper.utility.JsonReader import JSONFileManager
from helper.utility.ScreenshotUtils import capture_and_attach_screenshot

@allure.epic("User Account")
@allure.feature("Registration")
@allure.story("Create Account")
@scenario('../features/CreateAccount.feature', 'Create an account with valid and unique email ID')
def test_create_account():
    """Test create account scenario"""
    pass

@given('User is on the home page')
@allure.step("Navigate to the home page")
def user_in_home_page(page):
    """Ensure user is on the home page (handled by page fixture)"""
    # Page is already navigated to base_url by conftest.py
    capture_and_attach_screenshot(
        page=page,
        scenario_name="Create an account with valid and unique email id",
        step_name="User is on the home page"
    )
    return page

@when('User navigates to create account page')
@allure.step("Navigate to create account page")
def navigate_to_create_account_page(page, create_account):
    """Click the 'Create an Account' link"""
    create_account.navigate_to_create_account()
    capture_and_attach_screenshot(
        page=page,
        scenario_name="Create an account with valid and unique email id",
        step_name="User navigates to create account page"
    )


@when('User fills the registration form with valid data')
@allure.step("Fill registration form with valid data")
def enter_user_details(page, create_account, random_data):
    """Enter valid user details from random_data"""
    create_account.fill_form(first_name=random_data["first name"],
                             last_name=random_data["last name"],
                             email=random_data["email"],
                             password=random_data["password"]
                             )
    capture_and_attach_screenshot(
        page=page,
        scenario_name="Create an account with valid and unique email id",
        step_name="User fills the registration form with valid data"
    )

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
    capture_and_attach_screenshot(
        page=page,
        scenario_name="Create an account with valid and unique email id",
        step_name="User submits the form"
    )


@then('User should see the account creation success message')
@allure.step("Verify account creation success message")
def verify_success_message(page, create_account):
    """Verify the account creation success message"""
    create_account.expect_success_message()
    capture_and_attach_screenshot(
        page=page,
        scenario_name="Create an account with valid and unique email id",
        step_name="User should see the account creation success message"
    )

