import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestOrder:
    @pytest.mark.parametrize("customer_data, entry_point", [
        (
            {
                "name": "Иван",
                "surname": "Петров",
                "address": "ул. Ленина 1",
                "metro": "Лубянка",
                "phone": "89991112233",
                "date": "01.05.2026",
                "rental_period": "сутки",
                "color": "black",
                "comment": "Позвонить за час"
            },
            "top"
        ),
        (
            {
                "name": "Мария",
                "surname": "Иванова",
                "address": "пр. Мира 10",
                "metro": "Парк культуры",
                "phone": "89223334455",
                "date": "10.05.2026",
                "rental_period": "трое суток",
                "color": "grey",
                "comment": "Домофон 123"
            },
            "bottom"
        ),
    ])
    def test_positive_order_flow(self, driver, customer_data, entry_point):
        home_page = HomePage(driver)
        
        if entry_point == "top":
            home_page.click_order_top()
        else:
            home_page.click_order_bottom()
        
        order_page = OrderPage(driver)
        
        order_page.fill_name(customer_data["name"])
        order_page.fill_surname(customer_data["surname"])
        order_page.fill_address(customer_data["address"])
        order_page.fill_metro(customer_data["metro"])
        order_page.fill_phone(customer_data["phone"])
        order_page.click_next()
        
        order_page.fill_second_form(
            customer_data["date"],
            customer_data["rental_period"],
            customer_data["color"],
            customer_data["comment"]
        )
        order_page.click_order()
        order_page.confirm_order()
        
        success_msg = order_page.get_success_message()
        assert "Заказ оформлен" in success_msg
        