import os.path
from datetime import datetime
from pathlib import Path
from typing import Literal

import allure
from playwright.sync_api import Page, Locator, expect, Response


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
            exact: bool = True
    ):
        """Clicks link, opens new tab, asserts heading using flexible strategy, closes tab"""
        with self.page.context.expect_page() as new_tab:
            link_locator.click()
        new_page = new_tab.value
        new_page.wait_for_load_state("load")

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



    def notes_verify(self, expected_text: str = "Magento 2 Store(Sandbox site") -> None:
        """Click Notes link, handle new tab, assert page and close tab"""
        # Wait for the new tab to open
        # with self.page.context.expect_page() as new_page_info:
        #     self.notes.click()
        # new_page = new_page_info.value
        # new_page.wait_for_load_state("load")
        # # Assert
        # heading = new_page.get_by_role("heading", name=expected_text)
        # expect(heading).to_contain_text(expected_text)
        # new_page.close()
        self.verify_link_opens_correct_tab(
            link_locator=self.notes,
            expected_text="Magento 2 Store(Sandbox site) – Notes",
            locator_strategy="css_xpath_locator",
            locator_value=".alignwide.wp-block-post-title"
        )

    def write_for_us_verify(self, expected_text: str = "Write For Us") -> None:
        """Click Write for us link, handle new tab, assert page, and close tab"""
        # with self.page.context.expect_page() as new_page_info:
        #     self.write_for_us.click()
        # new_page = new_page_info.value
        # new_page.wait_for_load_state("load")
        # # Assert
        # expect(self.write_for_us_assert).to_contain_text(expected_text)
        # new_page.close()
        self.verify_link_opens_correct_tab(
            link_locator=self.write_for_us,
            expected_text="Write For Us",
            locator_strategy="role",
            locator_value="heading"
        )

    def subscribe_verify(self, expected_text: str = "Subscribe") -> None:
        """Click Subscribe link, handle new tab, assert page, and close tab"""
        # with self.page.context.expect_page() as new_page_info:
        #     self.subscribe.click()
        # new_page = new_page_info.value
        # new_page.wait_for_load_state("load")
        # # Assert
        # expect(self.write_for_us_assert).to_contain_text(expected_text)
        # new_page.close()
        self.verify_link_opens_correct_tab(
            link_locator=self.subscribe,
            expected_text="Subscribe",
            locator_strategy="locator",
            locator_value="h1"
        )

    def search_terms_verify(self) -> None:
        self.search_terms.click()
        return self.page.go_back()

    def privacy_cookie_policy_verify(self, expected_text: str = "Privacy Policy") -> None:
        self.privacy_cookie_policy.click()
        # Assert
        expect(self.write_for_us_assert).to_contain_text(expected_text)
        self.page.go_back()

    def advance_search_verify(self, expected_text: str = "Advanced Search") -> None:
        self.advance_search.click()
        expect(self.write_for_us_assert).to_contain_text(expected_text)
        self.page.go_back()

    def whats_new_verify(self, expected_text: str = "What's New") -> None:
        self.whats_new.click()
        expect(self.write_for_us_assert).to_contain_text(expected_text)
        self.page.go_back()

    def sale_verify(self, expected_text: str = "Sale") -> None:
        self.sale.click()
        expect(self.write_for_us_assert).to_contain_text(expected_text)
        self.page.go_back()




