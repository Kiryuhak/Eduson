from selenium.webdriver.common.by import By

from conftest import *

class TestMain:
    def test_str_gsm_shop(self, browser):
        pages_main = PagesGSM(browser, "https://str.gsm.shop")
        pages_main.open() # Проверка открытия страницы
        pages_main.check_title() # Проверка заголовка страницы
        pages_main.check.logo() # Проверка отображения логотипа

    #
    # # Проверка отображения логотипа
    # logo_element = browser.find_element(By.CSS_SELECTOR, "div[class*=header__col--logo]")
    # assert logo_element.is_displayed()
    #
    # # Проверка отображения меню
    # main_menu_element = browser.find_element(By.CSS_SELECTOR, "ul[class*=categories__items]")
    # assert main_menu_element.is_displayed()
    #
    # # Проверка отображения каталога
    # catalog_element = browser.find_element(By.CSS_SELECTOR, "ul[class*=categories__items]")
    # assert catalog_element.is_displayed()
    #
    # # Проверка работы поиска по товару
    # search_input = find_element(By.CSS_SELECTOR, By.CSS_SELECTOR, "input[class*=search__input]").send_keys(city)
    # search_input.send_keys("iPhone 13")
    # search_button = wait_for_element_visibility(browser, By.CSS_SELECTOR, "input[class*=search__submit]")
    # search_button.click()

    # def search(self, city):
    #     self.driver.find_element(By.CSS_SELECTOR, 'input[class*=input]').send_keys(city)
    #     wait = WebDriverWait(self.driver, 30)
    #     wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'found')))
    #     self.driver.find_element(By.CSS_SELECTOR, 'input[class*=input]').send_keys(Keys.ENTER)