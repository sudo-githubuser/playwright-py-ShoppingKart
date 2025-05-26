from playwright.sync_api import Page, expect


class CreateAccountPage:

    def __init__(self, page:Page):
        self.page = page
        self._init_locators()

    def _init_locators(self):
        self.create_account_btn = self.page.locator("header a[href*='customer/account/create']")
        self.first_name_input = self.page.get_by_label("First Name")
        self.last_name_input = self.page.get_by_label("Last Name")
        self.email_input = self.page.get_by_label("Email")
        self.password_input = self.page.locator('#password')
        self.confirm_pwd_input = self.page.locator('#password-confirmation')
        self.submit_btn = self.page.locator("button[type='submit']").nth(1)
        self.success_msg = self.page.locator("div.message-success")

    def navigate_to_create_account(self) -> None:
        self.create_account_btn.click()

    def fill_form(
            self,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
            confirm_password: str = None
    ) -> None:
        """
        Fill registration form with provided data
        Args:
            confirm_password: Optional, defaults to same as password
            :param confirm_password:
            :param password:
            :param email:
            :param last_name:
            :param first_name:
        """
        confirm_password = confirm_password or password
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_pwd_input.fill(confirm_password)

    def submit_form(self) -> None:
        self.submit_btn.click()

    # --- Assertions ---
    def expect_success_message(self, expected_text: str = "Thank you for registering") -> None:
        expect(self.success_msg).to_contain_text(expected_text)




