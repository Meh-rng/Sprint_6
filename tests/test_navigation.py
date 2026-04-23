from pages.home_page import HomePage
from constants import MAIN_PAGE_URL, DZEN_URL, YANDEX_URL, ORDER_ENDPOINT


class TestNavigation:
    def test_scooter_logo_redirects_to_main(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_top()
        home_page.wait_for_url_contains(ORDER_ENDPOINT)
        home_page.click_scooter_logo()
        home_page.wait_for_url_to_be(MAIN_PAGE_URL)
        assert home_page.get_current_url() == MAIN_PAGE_URL

    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        home_page = HomePage(driver)
        original_window = home_page.get_current_window_handle()
        home_page.click_yandex_logo()
        home_page.switch_to_new_window(original_window)
        home_page.wait_for_url_contains(DZEN_URL)
        assert DZEN_URL in home_page.get_current_url() or YANDEX_URL in home_page.get_current_url()
