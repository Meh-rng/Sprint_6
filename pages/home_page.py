from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators

    def click_order_top(self):
        self.click_element(self.locators.ORDER_TOP)

    def click_order_bottom(self):
        self.click_element(self.locators.ORDER_BOTTOM)

    def click_scooter_logo(self):
        self.click_element(self.locators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.locators.YANDEX_LOGO)

    def click_question(self, index):
        self.click_element_by_index(self.locators.FAQ_QUESTIONS, index)
        # Ждём появления ответа
        self.wait_for_text_not_empty(self.locators.FAQ_ANSWERS, index)

    def get_answer_text(self, index):
        self.wait_for_text_not_empty(self.locators.FAQ_ANSWERS, index)
        return self.get_text_by_index(self.locators.FAQ_ANSWERS, index)
      