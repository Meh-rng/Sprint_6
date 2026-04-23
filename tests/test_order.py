from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestOrder:
    # Данные для первого теста (верхняя кнопка, чёрный самокат)
    customer_data_top = {
        "name": "Иван",
        "surname": "Петров",
        "address": "ул. Ленина 1",
        "metro": "Лубянка",
        "phone": "89991112233",
        "date": "01.05.2026",
        "rental_period": "сутки",
        "color": "black",
        "comment": "Позвонить за час"
    }

    # Данные для второго теста (нижняя кнопка, серый самокат)
    customer_data_bottom = {
        "name": "Мария",
        "surname": "Иванова",
        "address": "пр. Мира 10",
        "metro": "Парк культуры",
        "phone": "89223334455",
        "date": "10.05.2026",
        "rental_period": "трое суток",
        "color": "grey",
        "comment": "Домофон 123"
    }

    def test_positive_order_flow_top_black(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_top()
        home_page.wait_for_url_contains("/order")
        
        order_page = OrderPage(driver)
        order_page.fill_name(self.customer_data_top["name"])
        order_page.fill_surname(self.customer_data_top["surname"])
        order_page.fill_address(self.customer_data_top["address"])
        order_page.fill_metro(self.customer_data_top["metro"])
        order_page.fill_phone(self.customer_data_top["phone"])
        order_page.click_next()
        order_page.wait_for_date_field()
        order_page.fill_second_form(
            self.customer_data_top["date"],
            self.customer_data_top["rental_period"],
            self.customer_data_top["color"],
            self.customer_data_top["comment"]
        )
        order_page.click_order()
        order_page.confirm_order()
        assert order_page.is_success_message_displayed()

    def test_positive_order_flow_bottom_grey(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_bottom()
        home_page.wait_for_url_contains("/order")
        
        order_page = OrderPage(driver)
        order_page.fill_name(self.customer_data_bottom["name"])
        order_page.fill_surname(self.customer_data_bottom["surname"])
        order_page.fill_address(self.customer_data_bottom["address"])
        order_page.fill_metro(self.customer_data_bottom["metro"])
        order_page.fill_phone(self.customer_data_bottom["phone"])
        order_page.click_next()
        order_page.wait_for_date_field()
        order_page.fill_second_form(
            self.customer_data_bottom["date"],
            self.customer_data_bottom["rental_period"],
            self.customer_data_bottom["color"],
            self.customer_data_bottom["comment"]
        )
        order_page.click_order()
        order_page.confirm_order()
        assert order_page.is_success_message_displayed()
