import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_dropdown_list(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("#dropdown").select_option("1")
    page.locator("#dropdown").press("Enter")
    page.locator("#dropdown").select_option("2")
    page.close()

    # ---------------------
    context.close()
    browser.close()
