from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    ORDER_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    FAQ_QUESTIONS = (By.CSS_SELECTOR, ".accordion__button")
    FAQ_ANSWERS = (By.CSS_SELECTOR, ".accordion__panel")

    def __init__(self, driver):
        self.driver = driver

    def click_order_top(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ORDER_TOP))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_order_bottom(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ORDER_BOTTOM))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_scooter_logo(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SCOOTER_LOGO))
        self.driver.execute_script("arguments[0].click();", element)

    def click_yandex_logo(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.YANDEX_LOGO))
        self.driver.execute_script("arguments[0].click();", element)

    def click_question(self, index):
        questions = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.FAQ_QUESTIONS)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", questions[index])
        self.driver.execute_script("arguments[0].click();", questions[index])
        # Не ждём видимости, просто небольшая пауза
        import time
        time.sleep(0.5)

    def get_answer_text(self, index):
        # Ждём, пока у элемента появится непустой текст
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(*self.FAQ_ANSWERS)[index].text) > 0
        )
        answers = self.driver.find_elements(*self.FAQ_ANSWERS)
        return answers[index].text
    