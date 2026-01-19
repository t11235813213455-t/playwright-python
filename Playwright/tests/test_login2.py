import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_login2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://webdriveruniversity.com/Login-Portal/index.html?")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Tatiana")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("pass123")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Login").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()
