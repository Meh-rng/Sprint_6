from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    FAQ_QUESTIONS = (By.CSS_SELECTOR, ".accordion__button")
    FAQ_ANSWERS = (By.CSS_SELECTOR, ".accordion__panel")
    