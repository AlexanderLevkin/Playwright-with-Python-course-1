from playwright.sync_api import Playwright, expect
import pytest

def test_add_todo(page):
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/", wait_until='domcontentloaded')
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")


@pytest.mark.skip_browser("firefox")
def test_visit_example(page):
    page.goto("https://example.com")


@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")