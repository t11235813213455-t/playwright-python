import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_upload_file(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice-automation.com/file-upload/")
    page.get_by_role("button", name="Choose File").click()
    page.get_by_role("button", name="Choose File").set_input_files("test.txt")
    page.get_by_role("button", name="Upload").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()
