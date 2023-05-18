def test_loc(page):
    page.goto('https://textinput.antonzimaiev.repl.co/?')
    page.get_by_label("Email address").fill("qa@example.com")
    page.get_by_title("username").fill("Anton")
    page.get_by_placeholder('password').fill("secret")
    page.get_by_role('checkbox').click()
    page.get


""" 
Фильтрация
Для того чтобы помочь локализовать поиск,
реализован метод filter(). Сузить поиск можно передав аргументом фильтр по тексту,
по локатору или можно использовать оба способа фильтрации.

Для того чтобы отфильтровать элементы по тексту,
нужно передать префикс has_text=  и текст, который присутствует в элементе.
"""

page.locator("li").filter(has_text='Company').click()

#  Для того чтобы отфильтровать элементы по локатору, используйте префикс has=

page.locator('li').filter(has=page.locator('.dropdown-toggle')).click()

# Работа с несколькими элементами

# Если вам необходимо узнать количество элементов, соответствующих указанному селектору - используйте метод count()

page.get_by_role("button").count()

# Для того чтобы взаимодействовать с конкретным элементом из списка, используйте метод nth()
# с указанием индекса нужного вам элемента.

page.get_by_role("listitem").nth(1)