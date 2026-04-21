import time
from pages.home_page import HomePage


class TestNavigation:
    def test_scooter_logo_redirects_to_main(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_top()
        time.sleep(1)
        home_page.click_scooter_logo()
        time.sleep(1)
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        home_page = HomePage(driver)
        original_window = driver.current_window_handle
        home_page.click_yandex_logo()
        time.sleep(2)
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        assert "dzen.ru" in driver.current_url or "yandex.ru" in driver.current_url
        