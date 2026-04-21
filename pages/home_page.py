from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    ORDER_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    FAQ_QUESTIONS = (By.CLASS_NAME, "accordion__button")
    FAQ_ANSWERS = (By.CLASS_NAME, "accordion__panel")

    def __init__(self, driver):
        self.driver = driver

    def click_order_top(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ORDER_TOP))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_order_bottom(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ORDER_BOTTOM))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_scooter_logo(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SCOOTER_LOGO)).click()

    def click_yandex_logo(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.YANDEX_LOGO)).click()

    def click_question(self, index):
        questions = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.FAQ_QUESTIONS)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", questions[index])
        self.driver.execute_script("arguments[0].click();", questions[index])
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.FAQ_ANSWERS)
        )

    def get_answer_text(self, index):
        answers = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.FAQ_ANSWERS)
        )
        return answers[index].text
    