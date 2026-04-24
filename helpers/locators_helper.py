from selenium.webdriver.common.by import By

def get_rental_period_option(rental_period):
    return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{rental_period}']")