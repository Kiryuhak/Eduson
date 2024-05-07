from playwright.sync_api import Page

def test_page(playwright, page: Page):
    # Запуск браузера
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()

    # Переход на страницу
    page.goto("https://str.gsm.shop/")

    # Ввод логина и пароля
    page.locator("#login_form-login").fill('admin@admin.com')
    page.locator("#login_form-password").fill('admin')
    page.click('input[type=submit]')

    # Проверка успешной авторизации
    page.goto("https://str.gsm.shop/accounts")
    title_element = page.locator('h1[class*=personalpage__title]')
    assert title_element.text_content() == "Личный кабинет"

    # Закрытие браузера
    chromium.close()