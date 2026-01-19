import re
from playwright.sync_api import Playwright, sync_playwright, expect
import allure

@allure.epic("Web interface")
@allure.feature("Основные функции")
@allure.story("Добавление пунктов в чек-лист")
def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=50) # запуск браузера chromium
    context = browser.new_context() # создает изолированный сеанс браузера
    page = context.new_page() # открывает новую страницу(tab) в браузере

    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").fill("1")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("2")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("3")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("listitem").filter(has_text="1").get_by_label("Toggle Todo").check()
    page.get_by_role("listitem").filter(has_text="2").get_by_label("Toggle Todo").check()
    page.get_by_role("listitem").filter(has_text="3").get_by_label("Toggle Todo").check()

    # ---------------------
    context.close()
    browser.close()
