import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_popups(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice-automation.com/popups/")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Alert Popup").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm Popup").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Prompt Popup").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()
