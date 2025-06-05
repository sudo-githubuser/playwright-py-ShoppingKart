from playwright.sync_api import Page, Locator, expect


class HomePageHyperLink:

    def __init__(self, page:Page):
        self.page = page
        self._init_locators()

    def _init_locators(self):
        # On click locators
        self.notes = self.page.get_by_role("link", name="Notes")
        self.write_for_us = self.page.get_by_role("link", name="Write for us")
        self.subscribe = self.page.get_by_role("link", name="Subscribe")
        self.search_terms = self.page.get_by_role("link", name="Search Terms")
        self.privacy_cookie_policy = self.page.get_by_role("link", name="Privacy and Cookie Policy")
        self.advance_search = self.page.get_by_role("link", name="Advanced Search")
        self.whats_new = self.page.get_by_role("menuitem", name="What's New")
        self.sale = self.page.get_by_role("menuitem", name="Sale")

        # --- Assertions ---
        self.notes_assert = self.page.get_by_role("heading", name="Magento 2 Store(Sandbox site")
        self.write_for_us_assert = self.page.get_by_role("heading", name="Write For Us")
        self.subscribe_assert = self.page.locator("h1").filter(has_text="Subscribe")
        # search terms page assertion needs to be added
        self.privacy_cookie_policy_assert = self.page.get_by_role("heading", name="Privacy Policy", exact=True).locator("span")
        self.advance_search_assert = self.page.get_by_role("heading", name="Advanced Search").locator("span")
        self.whats_new_assert = self.page.get_by_label("What's New").get_by_text("What's New")
        self.sale_assert = self.page.get_by_label("Sale").get_by_text("Sale")


    # Write a private method for assertion and call it on each onClick method and pass on the variable to assert
    def _assert_links(self, locator: Locator, assert_text: str, assertion_type: str = "text") -> None:
        """
        Generic assertion method for hyperlinks.
        Args:
            locator: Playwright Locator for the element to assert.
            assert_text: Expected text for 'text' assertion or boolean for 'visible'.
            assertion_type: Type of assertion ('text' or 'visible', default 'text').
        """
        try:
            if assertion_type == "text":
                expect(locator).to_contain_text(str(assert_text))
            elif assertion_type == "visible":
                expect(locator).to_be_visible() if assert_text else expect(locator).not_to_be_visible()
            else:
                raise ValueError(f"Unsupported assertion type: {assertion_type}")
        except AssertionError as e:
            raise AssertionError(f"Assertion failed for locator {locator} with text '{assert_text}' and type '{assertion_type}': "
                                 f"{str(e)}")

    def notes_verify(self) -> None:
        self.notes.click()

    def assert_notes(self) -> None:
        self._assert_links(self.notes_assert, "Magento 2 Store(Sandbox site)")

