import os.path
from pathlib import Path
from typing import Literal
from playwright.sync_api import Page, Locator, expect, Response

from helper.utility.ScreenshotUtils import capture_and_attach_screenshot


class HomePageHyperLink:

    def __init__(self, page:Page):
        self.page = page
        self._init_locators()
        self.screenshots_dir = os.path.join(Path(__file__).parent.parent.parent, "reports", "screenshots")

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

    def verify_link_opens_correct_tab(
            self,
            link_locator: Locator,
            expected_text: str,
            locator_strategy: Literal["role", "locator", "label", "css_xpath_locator"] = "role",
            locator_value: str = "",
            exact: bool = True,
            screenshot_name: str = "default"
    ):
        """Clicks link, opens new tab, asserts heading using flexible strategy, closes tab"""
        with self.page.context.expect_page() as new_tab:
            link_locator.click()
        new_page = new_tab.value
        new_page.wait_for_load_state("load")

        capture_and_attach_screenshot(
            page=new_page,
            scenario_name="Homepage hyperlinks",
            step_name=screenshot_name
        )

        # Dynamic locator resolution
        if locator_strategy == "role":
            target = new_page.get_by_role(locator_value, name=expected_text, exact=exact)
        elif locator_strategy == "locator":
            target = new_page.locator(locator_value).filter(has_text=expected_text)
        elif locator_strategy == "label":
            target = new_page.get_by_label(locator_value).get_by_text(expected_text)
        elif locator_strategy == "css_xpath_locator":
            target = new_page.locator(locator_value)
        else:
            raise ValueError(f"Unsupported locator strategy: {locator_strategy}")
        # Assertion
        expect(target).to_contain_text(expected_text)
        new_page.close()


    def notes_verify(self) -> None:
        self.verify_link_opens_correct_tab(
            link_locator=self.notes,
            expected_text="Magento 2 Store(Sandbox site) – Notes",
            locator_strategy="css_xpath_locator",
            locator_value=".alignwide.wp-block-post-title",
            screenshot_name = "Notes Page"
        )

    def write_for_us_verify(self) -> None:
        self.verify_link_opens_correct_tab(
            link_locator=self.write_for_us,
            expected_text="Write For Us",
            locator_strategy="role",
            locator_value="heading",
            screenshot_name = "Write for us Page"
        )

    def subscribe_verify(self) -> None:
        self.verify_link_opens_correct_tab(
            link_locator=self.subscribe,
            expected_text="Subscribe",
            locator_strategy="locator",
            locator_value="h1",
            screenshot_name = "Subscribe Page"
        )

    def search_terms_verify(self) -> None:
        self.search_terms.click()
        return self.page.go_back()

    def privacy_cookie_policy_verify(self) -> None:
        self.verify_link_opens_correct_tab(
            link_locator=self.privacy_cookie_policy,
            expected_text="Privacy and Cookie Policy",
            locator_strategy="role",
            locator_value="link",
            screenshot_name = "Privacy policy Page"
        )

    def advance_search_verify(self) -> None:
        self.verify_link_opens_correct_tab(
            link_locator=self.advance_search,
            expected_text="Advanced Search",
            locator_strategy="role",
            locator_value="link",
            screenshot_name = "Advance Search Page"
        )

    def whats_new_verify(self) -> None:
        self.verify_link_opens_correct_tab(
            link_locator=self.whats_new,
            expected_text="What's New",
            locator_strategy="role",
            locator_value="menuitem",
            screenshot_name = "What's New Page"
        )

    def sale_verify(self) -> None:
        self.verify_link_opens_correct_tab(
            link_locator=self.sale,
            expected_text="Sale",
            locator_strategy="role",
            locator_value="menuitem",
            screenshot_name = "Sales Page"
        )




