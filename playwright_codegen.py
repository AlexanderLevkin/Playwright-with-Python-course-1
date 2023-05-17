from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://www.onliner.by/")
    page.wait_for_load_state("networkidle")
    page.get_by_text("Вход").click()
    page.get_by_placeholder("Ник или e-mail").click()
    page.get_by_placeholder("Ник или e-mail").fill("Hello")
    page.get_by_placeholder("Пароль").click()
    page.get_by_placeholder("Пароль").fill("gotit")
    page.locator("#auth-container").get_by_text("Войти").click()

    page.frame_locator("iframe[name=\"a-61od1coj0jtj\"]").get_by_role("checkbox", name="Я не робот").click()

    expect(page.get_by_role("checkbox", name="Я не робот")).to_be_disabled()
    print("yep")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
