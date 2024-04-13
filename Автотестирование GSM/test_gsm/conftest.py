import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    """Фикстура для открытия браузера."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def wait_for_element_visibility(browser, locator):
    """
    Функция для ожидания видимости элемента.
    browser: Экземпляр драйвера браузера.
    locator: Локатор элемента.
    """
    return WebDriverWait(browser, 10).until(EC.visibility_of_element_located(locator))


class PagesGSM:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def check_title(self):
        assert self.driver.title == "Купить запчасти и аксессуары для мобильных устройств в Стерлитамак-GSM"

    def check_logo(self):
        logo = self.driver.find_element_by_class_name("logo")
        assert logo.text == "Стерлитамак-GSM"

    # def search(self, element):
    #     self.driver.find_element(By.CSS_SELECTOR, 'input[class*=input]').send_keys(element)
    #     wait = WebDriverWait(self.driver, 30)
    #     wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'found')))
    #     self.driver.find_element(By.CSS_SELECTOR, 'input[class*=input]').send_keys(Keys.ENTER)
