from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class OrderPage:
    
    # Первая форма — по индексу полей
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder= '* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    
    # Вторая форма
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    def __init__(self, driver):
        self.driver = driver

    def fill_name(self, name):
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)

    def fill_surname(self, surname):
        self.driver.find_element(*self.SURNAME_FIELD).send_keys(surname)

    def fill_address(self, address):
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)

    def fill_metro(self, metro):
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.METRO_FIELD)
    )
        field.click()
        field.send_keys(metro)
        
        station = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'select-search__select')]//li"))
    )
        station.click()
        

    def fill_phone(self, phone):
        
        field = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.PHONE_FIELD)
    )
        field.clear()
        field.send_keys(phone)

    def click_next(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_date(self, date):
        field = self.driver.find_element(*self.DATE_FIELD)
        field.send_keys(date)
        field.send_keys(Keys.RETURN)

    def select_rental_period(self, period):
        self.driver.find_element(*self.RENTAL_DROPDOWN).click()
        period_option = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']")
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(period_option)
        ).click()

    def select_color(self, color):
        if color.lower() == "black":
            self.driver.find_element(*self.COLOR_BLACK).click()
        elif color.lower() == "grey":
            self.driver.find_element(*self.COLOR_GREY).click()

    def fill_comment(self, comment):
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(comment)

    def click_order(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ORDER_BUTTON))
        self.driver.execute_script("arguments[0].click();", element)

    def confirm_order(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CONFIRM_BUTTON))
        self.driver.execute_script("arguments[0].click();", element)

    def get_success_message(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text

    # Комбинированные методы
    def fill_first_form(self, name, surname, address, metro, phone):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.NAME_FIELD)
    )
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
        