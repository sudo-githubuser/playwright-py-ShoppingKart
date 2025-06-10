import os
from datetime import datetime
from pathlib import Path

import allure
from playwright.sync_api import Page

PROJECT_ROOT = Path(__file__).parent.parent.parent
print(f"StepDef PROJECT_ROOT: {PROJECT_ROOT}")
screenshots_dir = os.path.join(PROJECT_ROOT, "reports", "screenshots")

def capture_and_attach_screenshot(
        page: Page,
        scenario_name: str,
        step_name: str
) -> None:
    """Captures and attaches a screenshot to Allure"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    step_name = step_name.replace(" ", "_").lower()
    scenario_name = scenario_name.replace(" ", "_").lower()
    screenshot_name = f"{scenario_name}_{step_name}_{timestamp}.png"
    screenshot_path = os.path.join(screenshots_dir, screenshot_name)

    try:
        page.screenshot(path=screenshot_path, full_page=True)
        with open(screenshot_path, 'rb') as image_file:
            allure.attach(
                body=image_file.read(),
                name=screenshot_name,
                attachment_type=allure.attachment_type.PNG
            )
        print(f"Screenshot saved: {screenshot_path}")
    except Exception as e:
        print(f"Failed to capture screenshot: {e}")