from conftest import PagesGis


class TestSnow:

    def test_snow_in_gismeteo(self, browser, set_city_str, set_city_ufa):
        pages_main = PagesGis(browser, "https://www.gismeteo.ru/")
        # pages_main.open()
        # pages_main.search("Стерлитамак")
        # pages_main.set_tomorrow()
        # pages_main.set_snow()
