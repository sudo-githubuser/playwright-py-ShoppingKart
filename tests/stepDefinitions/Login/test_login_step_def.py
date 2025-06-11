import allure
from pytest_bdd import scenario, given, when, then
from helper.utility.JsonReader import JSONFileManager
from helper.utility.ScreenshotUtils import capture_and_attach_screenshot

@allure.epic("User Account")
@allure.feature("Login")
@allure.story("Login with valid email ID")
@scenario('../features/Login.feature', 'Login with valid user credentials')
def test_login():
    """Test login scenario"""
    pass

@given('User is on the home page')
@allure.step("Navigate to the home page")
def user_in_home_page(page):
    """Ensure user is on the home page (handled by page fixture)"""
    # Page is already navigated to base_url by conftest.py
    capture_and_attach_screenshot(
        page=page,
        step_name="User is on the home page"
    )
    return page

@when('User navigates to login page')
@allure.step("Navigate to login page")
def navigate_to_login_page(page, login):
    """Click the 'Create an Account' link"""
    login.navigate_to_login_page()
    login.expect_login_page_message()
    capture_and_attach_screenshot(
        page=page,
        step_name="User navigates to login page"
    )

@given('User enters valid email address, password')
@allure.step('Enter valid email ID and password')
def enter_valid_email_address(page, login, random_data):
    json_manager = JSONFileManager()
    credentials = json_manager.get_credentials()
    login.enter_credentials(credentials["email"], credentials["password"])
    capture_and_attach_screenshot(
        page=page,
        step_name="User enters valid email address, password"
    )

@when('User clicks on sign in')
@allure.step('Click on Sign In button')
def sign_in(page, login):
    login.user_login()
    capture_and_attach_screenshot(
        page=page,
        step_name="User clicks on sign in"
    )

@then('Home page is displayed')
@allure.step('User logged in successfully')
def verify_sign_in(page, login):
    login.expect_home_page_message()
    capture_and_attach_screenshot(
        page=page,
        step_name="Home page is displayed"
    )

@then('User is logged out')
def user_logout(page, login):
    login.user_logout()
    capture_and_attach_screenshot(
        page=page,
        step_name="User logged out"
    )



