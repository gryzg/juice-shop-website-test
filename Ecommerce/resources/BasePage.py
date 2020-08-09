#---Parent Class
#---Common functionalities and elements

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage():
    TIME_WAIT = 10

    def __init__(self, driver):
        driver = self.driver

    def element_is_visible(driver, locator_by, locator):
        wait = WebDriverWait(driver, BasePage.TIME_WAIT)
        element = wait.until(ec.visibility_of_element_located((locator_by, locator)))
        return bool(element)

    def element_is_enabled(driver, locator_by, locator):
        return  WebDriverWait(driver,BasePage.TIME_WAIT).until(ec.visibility_of_element_located((locator_by, locator)))

    def assert_element_text(expected_text, actual_text):
        print ("Expected: " + expected_text)
        print ("Actual: " + actual_text)

        assert expected_text == actual_text



