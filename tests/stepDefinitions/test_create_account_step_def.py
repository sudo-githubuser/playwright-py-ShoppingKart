from pytest_bdd import scenario, given, when, then

from pageObjects.objectRepository.CreateAccount import CreateAccountPage


@scenario('../features/CreateAccount.feature', 'Create an account with valid and unique email ID')
def test_create_account():
    """Test the create account scenario"""
    pass

@given('User is on the home page')
def user_in_home_page(page):
    """Ensure user is on the home page (handled by page fixture)"""
    # Page is already navigated to base_url by conftest.py
    return page

@when('User navigates to create account page')
def navigate_to_create_account_page(page, create_account):
    """Click the 'Create an Account' link"""
    #create_account = CreateAccountPage(page)
    create_account.navigate_to_create_account()
    #return create_account

@when('User fills the registration form with valid data')
def enter_user_details(create_account, random_data):
    """Enter valid user details from random_data"""
    create_account.fill_form(first_name=random_data["first name"],
                             last_name=random_data["last name"],
                             email=random_data["email"],
                             password=random_data["password"]
                             )

@when('User submits the form')
def submit_form(create_account):
    """Submit the account creation form"""
    create_account.submit_form()

@then('User should see the account creation success message')
def verify_success_message(create_account):
    """Verify the account creation success message"""
    create_account.expect_success_message()

