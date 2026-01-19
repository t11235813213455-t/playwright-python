import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/tables#edit")
    page.get_by_role("link", name="edit").first.click()
    page.get_by_role("link", name="delete").first.click()
    page.get_by_role("link", name="delete").nth(2).click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
