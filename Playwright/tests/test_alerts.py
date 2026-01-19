import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_alerts(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://webdriveruniversity.com/Popup-Alerts/index.html")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator("#button1").click()
    page.locator("#button2").get_by_text("CLICK ME!").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("link", name="CLICK ME!").click()
    page.get_by_text("CLICK ME!").click()
    page.get_by_role("button", name="Close").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator("#button4").get_by_text("CLICK ME!").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()
