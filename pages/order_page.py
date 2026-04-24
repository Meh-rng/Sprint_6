from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from helpers.locators_helper import get_rental_period_option

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    def fill_name(self, name):
        self.send_keys(self.locators.NAME_FIELD, name)

    def fill_surname(self, surname):
        self.send_keys(self.locators.SURNAME_FIELD, surname)

    def fill_address(self, address):
        self.send_keys(self.locators.ADDRESS_FIELD, address)

    def fill_metro(self, metro):
        field = self.find_element(self.locators.METRO_FIELD)
        field.click()
        field.send_keys(metro)
        station = self.find_element(self.locators.METRO_STATION)
        station.click()

    def fill_phone(self, phone):
        self.send_keys(self.locators.PHONE_FIELD, phone)

    def click_next(self):
        self.click_element(self.locators.NEXT_BUTTON)

    def fill_date(self, date):
        field = self.find_element(self.locators.DATE_FIELD)
        field.send_keys(date)
        field.send_keys(Keys.RETURN)

    def select_rental_period(self, rental_period):
        self.click_element(self.locators.RENTAL_DROPDOWN)
        period_option = get_rental_period_option(rental_period)
        self.wait_and_click(period_option, timeout=3)

    def select_color(self, color):
       colors = {
            "black": self.locators.COLOR_BLACK,
            "grey": self.locators.COLOR_GREY
       }
       self.click_element(colors[color.lower()])

    def fill_comment(self, comment):
        self.send_keys(self.locators.COMMENT_FIELD, comment)

    def click_order(self):
        self.click_element(self.locators.ORDER_BUTTON)

    def confirm_order(self):
        self.click_element(self.locators.CONFIRM_BUTTON)

    def is_success_message_displayed(self):
        return self.find_element(self.locators.SUCCESS_MESSAGE).is_displayed()

    def fill_first_form(self, name, surname, address, metro, phone):
        self.wait_for_text_not_empty(self.locators.NAME_FIELD, 0)
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.fill_metro(metro)
        self.fill_phone(phone)

    def fill_second_form(self, date, rental_period, color, comment):
        self.fill_date(date)
        self.select_rental_period(rental_period)
        self.select_color(color)
        self.fill_comment(comment)
    
    def wait_for_date_field(self):
        self.wait_for_element_visible(self.locators.DATE_FIELD)
