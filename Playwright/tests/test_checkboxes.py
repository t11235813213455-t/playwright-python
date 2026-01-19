import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_checkboxes(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.get_by_role("checkbox").first.check()
    page.get_by_role("checkbox").nth(1).uncheck()
    page.close()

    # ---------------------
    context.close()
    browser.close()
