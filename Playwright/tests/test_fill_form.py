import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_fill_form(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://webdriveruniversity.com/Contact-Us/contactus.html")
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("Tatiana")
    page.get_by_role("textbox", name="First Name").press("Tab")
    page.get_by_role("textbox", name="Last Name").fill("Y")
    page.get_by_role("textbox", name="Last Name").press("Tab")
    page.get_by_role("textbox", name="Email Address").fill("mail@mail.ru")
    page.get_by_role("textbox", name="Email Address").press("Tab")
    page.get_by_role("textbox", name="Comments").fill("Hello! Thanks!")
    page.get_by_role("button", name="SUBMIT").click()
    page.get_by_role("heading", name="Thank You for your Message!").click()
    page.get_by_role("heading", name="Thank You for your Message!").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()
