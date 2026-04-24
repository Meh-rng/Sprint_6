from pages.home_page import HomePage
from pages.order_page import OrderPage
from data.order_data import customer_data_top, customer_data_bottom


class TestOrder:
    def test_positive_order_flow_top_black(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_top()
        home_page.wait_for_url_contains("/order")
        
        order_page = OrderPage(driver)
        order_page.fill_name(customer_data_top["name"])
        order_page.fill_surname(customer_data_top["surname"])
        order_page.fill_address(customer_data_top["address"])
        order_page.fill_metro(customer_data_top["metro"])
        order_page.fill_phone(customer_data_top["phone"])
        order_page.click_next()
        order_page.wait_for_date_field()
        order_page.fill_second_form(
            customer_data_top["date"],
            customer_data_top["rental_period"],
            customer_data_top["color"],
            customer_data_top["comment"]
        )
        order_page.click_order()
        order_page.confirm_order()
        assert order_page.is_success_message_displayed()

    def test_positive_order_flow_bottom_grey(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_bottom()
        home_page.wait_for_url_contains("/order")
        
        order_page = OrderPage(driver)
        order_page.fill_name(customer_data_bottom["name"])
        order_page.fill_surname(customer_data_bottom["surname"])
        order_page.fill_address(customer_data_bottom["address"])
        order_page.fill_metro(customer_data_bottom["metro"])
        order_page.fill_phone(customer_data_bottom["phone"])
        order_page.click_next()
        order_page.wait_for_date_field()
        order_page.fill_second_form(
            customer_data_bottom["date"],
            customer_data_bottom["rental_period"],
            customer_data_bottom["color"],
            customer_data_bottom["comment"]
        )
        order_page.click_order()
        order_page.confirm_order()
        assert order_page.is_success_message_displayed()