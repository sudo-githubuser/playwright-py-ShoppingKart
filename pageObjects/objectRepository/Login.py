from typing import Dict

from playwright.sync_api import Page, Playwright, expect

from helper.utility.JsonReader import JSONFileManager


class LoginPage:

    def __init__(self, page:Page):
        self.page = page
        self._init_locators()

    def _init_locators(self):
        self.sign_in_btn_home = self.page.get_by_role('link', name='Sign In')
        self.email_fill = self.page.get_by_role('textbox', name="Email*")
        self.password_fill = self.page.get_by_role("textbox", name="Password* Password")
        self.sign_in_btn_login = self.page.get_by_role('button', name='Sign In')

        #For Assertion
        self.login_page_text_check = self.page.get_by_text("Customer Login") #Login page assertion
        self.home_page_text_check = self.page.locator("div[class='panel header'] span[class='logged-in']") #Home page assertion

    def navigate_to_login_page(self) -> None:
        self.sign_in_btn_home.click()

    def enter_credentials(
            self,
            user_email: str,
            user_password: str = None
    ) -> None:
        self.email_fill.fill(user_email)
        self.password_fill.fill(user_password)

    def user_login(self) -> None:
        self.sign_in_btn_login.click()

    # --- Assertions ---
    def expect_login_page_message(self, expected_text: str = "Customer Login") -> None:
        expect(self.login_page_text_check).to_contain_text(expected_text)

    def expect_home_page_message(self, expected_text: str = "Welcome, {fn ln}!") -> None:
        """Assert the home page welcome message contains the expected text, using username from JSON"""
        json_manager: JSONFileManager = JSONFileManager()
        try:
            credentials: Dict[str, str] = json_manager.get_credentials()
            full_name: str = f"{credentials['first_name']} {credentials['last_name']}"
            # Replace {email_address} with full name
            formatted_text: str = expected_text.replace("{fn ln}", full_name)
            expect(self.home_page_text_check).to_contain_text(formatted_text)
        except ValueError as e:
            raise AssertionError(f"Failed to get credentials: {str(e)}")
        except KeyError as e:
            raise AssertionError(f"Missing credentials in JSON: {str(e)}")


