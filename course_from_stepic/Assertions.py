"""
В свою очередь условие проверки может иметь два варианта записи:
"""
from playwright.sync_api import expect

# Вариант 1
# expect(locator).not_to_be_checked()
#
# # Использовать проверку без передачи в нее аргументов.
#
# Вариант 2
# expect(locator).not_to_contain_text(expected, **kwargs)
# expect(locator).not_to_have_attribute(name, value, **kwargs)

"""
Если указаны ожидаемые значения expected, name, value и т.д, то необходимо их передать для проверки.
Данные атрибуты определяют какие выражения, значения атрибутов мы будет сравнивать с фактическим результатом.
"""

def test_playwright_assertion(browser_context_args):
    page = browser_context_args
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url('https://demo.playwright.dev/todomvc/#/')
    fill_form = page.get_by_placeholder('What needs to be done?')
    expect(fill_form).to_be_empty()
    fill_form.type('Задача №1')
    fill_form.press('Enter')
    fill_form.type('Задача №2')
    fill_form.press('Enter')
    page.pause()
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)
