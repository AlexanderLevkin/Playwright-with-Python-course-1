import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser_context_args():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        yield page
        page.close()
        browser.close()

