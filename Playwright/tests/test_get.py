import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test_get(page):
    response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
    print(response.status)
    print(response.json())
    print("My test")
