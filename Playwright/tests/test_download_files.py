import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_download_files(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice-automation.com/file-download/")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download").nth(2).click()
    download = download_info.value
    page.get_by_role("link", name="Download").nth(4).click()
    page.locator("#wpdm-lock-frame").content_frame.get_by_role("textbox", name="Enter Password").click()
    page.locator("#wpdm-lock-frame").content_frame.get_by_role("textbox", name="Enter Password").fill("automateNow")
    with page.expect_download() as download1_info:
        with page.expect_popup() as page1_info:
            page.locator("#wpdm-lock-frame").content_frame.get_by_role("button", name="Submit").click()
        page1 = page1_info.value
    download1 = download1_info.value
    page1.close()
    page.locator("#wpdm-lock-frame").content_frame.get_by_role("button", name="Close").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()
