import pytest
import time
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

@pytest.fixture(scope="function")
def set_city_str(browser):
    pages_main = PagesGis(browser, "https://www.gismeteo.ru/")
    pages_main.open()
    pages_main.search("Стерлитамак")

@pytest.fixture(scope="function")
def set_city_ufa(browser):
    pages_main = PagesGis(browser, "https://www.gismeteo.ru/")
    pages_main.open()
    pages_main.search("Уфа")

def wait_for_element_visibility(browser, locator):
    """
    Функция для ожидания видимости элемента.
    browser: Экземпляр драйвера браузера.
    locator: Локатор элемента.
    """
    return WebDriverWait(browser, 10).until(EC.visibility_of_element_located(locator))


class PagesGis:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def search(self, city):
        self.driver.find_element(By.CSS_SELECTOR, 'input[class*=input]').send_keys(city)
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'found')))
        self.driver.find_element(By.CSS_SELECTOR, 'input[class*=input]').send_keys(Keys.ENTER)

    def set_tomorrow(self):
        self.driver.find_element(By.XPATH, '//a[text()="Завтра "]').click()

    def set_snow(self):
        self.driver.find_element(By.XPATH, '//a[text()="Снег"]').click()
        time.sleep(5)

    def check_snow(self):
        self.driver.find_element(By.XPATH, '//a[text()="Снег"]').text
    #     #return self.driver.find_element(By.CLASS_NAME, 'chart.chart-snow)').find_element(By.XPATH, '/div/div[1]').get_attribute('innerHTML')
