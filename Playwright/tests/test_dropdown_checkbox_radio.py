import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test_dropdown_checkbox_radio(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
    page.locator("#dropdowm-menu-1").select_option("python")
    page.locator("#dropdowm-menu-2").select_option("maven")
    page.locator("#dropdowm-menu-3").select_option("jquery")
    page.get_by_role("radio").nth(5).check()
    page.get_by_role("checkbox", name="Option 1").check()
    page.get_by_role("checkbox", name="Option 2").check()
    page.get_by_role("checkbox", name="Option 3").uncheck()
    page.get_by_role("checkbox", name="Option 4").check()
    page.get_by_role("radio").nth(2).check()
    page.get_by_role("radio").nth(4).check()
    page.get_by_role("radio").first.check()
    page.get_by_role("radio").nth(1).check()
    page.get_by_role("radio").nth(3).check()
    page.locator("#main-header").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()
