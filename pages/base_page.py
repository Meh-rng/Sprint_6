from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.scroll_to_element(element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_element_by_index(self, locator, index, timeout=10):
        elements = self.find_elements(locator, timeout)
        self.scroll_to_element(elements[index])
        self.driver.execute_script("arguments[0].click();", elements[index])

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text

    def get_text_by_index(self, locator, index, timeout=10):
        elements = self.find_elements(locator, timeout)
        return elements[index].text

    def wait_for_text_not_empty(self, locator, index, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.find_elements(*locator)[index].text) > 0
        )
    def switch_to_new_window(self, original_window_handle):
        """Переключается на новую вкладку (не оригинальную)"""
        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(2)
    )
        for window_handle in self.driver.window_handles:
            if window_handle != original_window_handle:
                self.driver.switch_to.window(window_handle)
                break

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, url_part):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(url_part)
    )

    def wait_for_url_to_be(self, expected_url):
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(expected_url)
    )

    def wait_for_new_window(self):
        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(2)
    )    
    def wait_for_element_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
    )
        
    def wait_and_click(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
        EC.element_to_be_clickable(locator)
    ).click()   
         
    def get_current_window_handle(self):
        return self.driver.current_window_handle