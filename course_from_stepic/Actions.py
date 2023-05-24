import time

from playwright.sync_api import Page, Playwright

"""
Attached - элемент присоединен к DOM. Элемент считается прикрепленным, если он подключен к DOM или ShadowRoot.

Editable - элемент редактируемый. Элемент считается редактируемым, если он включен и у него не установлено свойство "read only".

Enabled - элемент включен. Считается включенным, если у тегов button, select, input, textare не имеют свойства disabled.

Receive Events - получает события, не заслоняемые другими элементами.

Stable - элемент стабилен. Элемент считается стабильным, если он сохраняет ту же  область после двух или более последовательных кадров анимации.

Visible -  элемент является видимым.

"""

# Если выполнение теста требует появление определенного элемента на странице,
# то вы можете указать playwright явно дождаться  элемента с помощью

# page.wait_for_selector()
"""
Если выполнение теста требует появление определенного элемента на странице,
то вы можете указать playwright явно дождаться  элемента с помощью
"""
# page.locator.check(**kwargs)

"""
Этот метод проверяет элемент, выполняя следующие действия:

    Проверяет, что элемент является checkbox или radio input.
    Ждет проверки элемента на пригодность к действию, если не установлен параметр force.
    При необходимости осуществляет скролл к  элементу, чтобы он был видим.
"""


# Давайте напишем сценарий, в котором мы по очереди нажимаем на все чекбоксы и радио-кнопки на сайте
def test_checkbox_with_check(browser_context_args):
    page = browser_context_args
    page.goto('https://checks-radios.antonzimaiev.repl.co/')
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()
    time.sleep(2)


def test_checkbox_with_click(browser_context_args):
    page = browser_context_args
    page.goto('https://checks-radios.antonzimaiev.repl.co/')
    page.locator("text=Default checkbox").click()
    page.locator("text=Checked checkbox").click()
    page.locator("text=Default radio").click()
    page.locator("text=Default checked radio").click()
    page.locator("text=Checked switch checkbox input").click()


# Dropdown menu

# locator.select_option(**kwargs)

"""
index - опции для выбора по индексу.В python, как и в любом языке программирования, индексы начинаются с ноля. 
По этому чтобы выбрать опцию - Предложил новую функцию, нужно указать индекс 1
value - для выбора по значению атрибута value.
label - выбор по текстовому значению
"""


def test_select(browser_context_args):
    page = browser_context_args.goto('https://select.antonzimaiev.repl.co/')
    page.select_option('#floatingSelect', value="3")
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")


def test_select_multiple(browser_context_args):
    page = browser_context_args.goto('https://select.antonzimaiev.repl.co/')
    page.goto('https://select.antonzimaiev.repl.co/')
    page.select_option('#skills', value=["playwright", "python"])
    time.sleep(3)




# Drag and Drop

# page.drag_and_drop(source, target, **kwargs)

def test_drag_and_drop(browser_context_args):
    page = browser_context_args
    page.goto('https://draganddrop.antonzimaiev.repl.co/')
    page.drag_and_drop("#drag", "#drop")
    time.sleep(2)


# Dialog windows

def test_dialogs(browser_context_args):
    page = browser_context_args
    page.goto("https://dialog.antonzimaiev.repl.co/")
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()


def test_dialog(browser_context_args):
    page = browser_context_args
    page.goto("https://dialog.antonzimaiev.repl.co/")
    page.on("dialog", lambda dialog: dialog.accept())
    # page.on -  прослушивает события которые, происходит в приложении.
    # dialog  -   анонимная функция обрабатывающая событие.
    # lambda dialog: dialog.accept() - анонимная функция обрабатывающая событие.
    page.get_by_text("Диалог Confirmation").click()


# Upload files

# method 1
def test_select_multip(browser_context_args):
    page = browser_context_args
    page.goto('https://upload.antonzimaiev.repl.co/')
    page.set_input_files("#formFile", "hello.txt")
    page.locator("#file-submit").click()

# method 2
def test_select_multi(browser_context_args):
    page = browser_context_args
    page.goto('https://upload.antonzimaiev.repl.co/')
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("hello.txt"))  # filechooser - обработчик событий
    page.locator("#formFile").click()


# method 3
def test_select_multiple(page):
    page.goto('https://upload.antonzimaiev.repl.co/')
    with page.expect_file_chooser() as fc_info:
        page.locator("#formFile").click()
    file_chooser = fc_info.value
    file_chooser.set_files("hello.txt")

"""
Получение значений элемента
Во время прохождения теста, вам может понадобиться извлечь данные с веб-страниц. К примеру  убедиться, что появилось
 сообщение для пользователя с определенным текстом.  

Вы можете получить текст веб-элемента двумя способами. Используя inner_text()
"""
element = page.locator('a:has-text("playwright")')
print(element.inner_text())
# or
element = page.locator('a:has-text("playwright")')
print(element.text_content())

"""
Используйте all_inner_text()  и all_text_contents() когда вам надо получить текст всех схожих элементов(например строк 
таблицы). В результате использования данных методов вернется массив значений для всех соответствующих элементов.
"""
page.goto('https://table.antonzimaiev.repl.co/')
row = page.locator("tr")
print(row.all_inner_texts())

page.goto('https://table.antonzimaiev.repl.co/')
row = page.locator("tr")
print(row.all_text_contents())


"""
textContent получает содержимое всех элементов, включая <script> и <style>, тогда как innerText этого не делает.
innerText умеет считывать стили и не возвращает содержимое скрытых элементов, тогда как textContent этого не делает.
"""

"""
Также кроме текста, можно получить HTML-код элемента.
"""
element = page.locator('a:has-text("playwright")')
print(element.inner_html())


"""
Работа с несколькими вкладками(Tabs)
"""

def test_new_tab(page: Page):
    page.goto("https://tabs.antonzimaiev.repl.co/")
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
    page.pause()
    assert new_tab.url == "https://tabs.antonzimaiev.repl.co/dashboard/index.html?"
    sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    assert sign_out.is_visible()
