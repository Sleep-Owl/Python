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

def open_brow():
    with sync_playwright() as op:
        browser = op.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://playwright.dev/')
        expect(page).to_have_title(re.compile('Playwright'))
        page.get_by_role('link', name='Get started').click()
        expect(page.get_by_role('heading', name='Installation'))
        page.screenshot(path='./demo.png')
        browser.close()


open_brow()

