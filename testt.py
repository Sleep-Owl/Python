import re
from playwright.sync_api import Page, expect, sync_playwright

# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))

# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def login_page():
    with sync_playwright() as sp:
        browser = sp.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://test02-tkp-lko.secgw.ru/#/login')
        expect(page).to_have_title(re.compile('ЛК ТКП'))
        expect(page.get_by_role('heading', name='Вход')).to_be_visible()

        # page.fill('input[placeholder="Логин"]', 'Admin')
        page.get_by_placeholder('Логин').fill('Admin')
        # page.fill('input[placeholder="Пароль"]', '123')
        page.get_by_placeholder('Пароль').fill('123')
        
        # page.get_by_role('button', name='Войти').click()
        page.click('text=Войти')
        expect(page.get_by_role('heading', name='Главная страница')).to_be_visible()
        page.screenshot(path='./demo.png')
        # browser.close()


login_page()

