import time
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
        
        # Клик по кнопке заказа
        if entry_point == "top":
            home_page.click_order_top()
        else:
            home_page.click_order_bottom()
        
        time.sleep(2)  # Ждём перехода на форму
        
        # Проверим, что мы на странице заказа (по URL или заголовку)
        print(f"\nТекущий URL: {driver.current_url}")
        
        order_page = OrderPage(driver)
        
        # Проверим, что поля существуют
        print("Ищем поле Имя...")
        order_page.fill_name(customer_data["name"])
        print("OK")
        
        print("Ищем поле Фамилия...")
        order_page.fill_surname(customer_data["surname"])
        print("OK")
        
        print("Ищем поле Адрес...")
        order_page.fill_address(customer_data["address"])
        print("OK")
        
        print("Ищем поле Метро...")
        order_page.fill_metro(customer_data["metro"])
        print("OK")
        
        print("Ищем поле Телефон...")
        order_page.fill_phone(customer_data["phone"])
        print("OK")
        
        print("Кнопка Далее...")
        order_page.click_next()
        print("OK")
        
        time.sleep(1)
        
        print("Заполняем вторую форму...")
        order_page.fill_second_form(
            customer_data["date"],
            customer_data["rental_period"],
            customer_data["color"],
            customer_data["comment"]
        )
        print("OK")
        
        order_page.click_order()
        order_page.confirm_order()
        
        success_msg = order_page.get_success_message()
        print(f"Сообщение: {success_msg}")
        assert "Заказ оформлен" in success_msg
        