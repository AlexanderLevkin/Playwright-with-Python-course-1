from playwright.sync_api import Page, Route, expect

"""
Для того чтобы начать прослушивать сеть, необходимо дать команду слушать события request и response и обрабатывать их
"""


def test_listen_network(browser_context_args):
    page = browser_context_args
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto('https://osinit.ru/')


"""
Рассмотрим вариант прерывания запросов к данным сайта, если это изображения  
"""
# page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())

"""
Представим, что нам необходимо изменить передаваемый данные.  Для этого используете метод  route.continue_  
и аргументом post_data
"""


def test_network(browser_context_args):
    page = browser_context_args
    page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
    page.goto('https://reqres.in/')
    page.get_by_text(' Register - successful ').click()



"""
На практике , намного чаще  требуется изменить ответ от сервера.
В автоматизации тестирования мокинг(подмена ответа от сервера) полезен для создания контролируемой среды тестирования. 
В качестве среды для тестирования мы будем использовать  веб-приложение блог -  realworld.io

Для  подмены ответа используется метод route.fulfill в котором указывается путь до json с подменными данными.
"""

def test_mock_tags(browser_context_args):
    page = browser_context_args
    page.route("*/api/tags", lambda route: route.fulfill(path="data.json"))
    page.goto('https://demo.realworld.io/')

"""
Метод route.fetch выполняет запрос на сервер и получает результат на данный запрос.  
Вы можете работать с полученным ответом как с json объектом.  
С помощью метода route.fulfill и опции json, отправьте запрос с исправленным телом ответа. 
В тестовом примере ниже, для выполнения трех этапов mocking создана функция-обработчик handle_route
"""
def test_intercepted(browser_context_args):
    page = browser_context_args
    def handle_route(route: Route):
        response = route.fetch()
        json = response.json()
        json["tags"] = ["open", "solutions"]
        route.fulfill(json=json)

    page.route("**/api/tags", handle_route)

    page.goto("https://demo.realworld.io/")
    sidebar = page.locator('css=div.sidebar')
    expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])