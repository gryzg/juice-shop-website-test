from selenium.webdriver.common.by import By
from selenium import webdriver

from resources.locators import Locators
from resources.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        driver = self.driver

    def get_logged_in_account (driver):
        driver.find_element_by_id(Locators.NAV_BAR_ACCOUNT_BTN).click()

        BasePage.element_is_visible(driver, By.XPATH, Locators.ACCOUNT_LOGGED_IN)
        account_logged_in = driver.find_element_by_xpath((Locators.ACCOUNT_LOGGED_IN))
        account_logged_in = account_logged_in.text
        return account_logged_in

    def add_to_cart(driver, order_item):
        BasePage.element_is_visible(driver, By.CLASS_NAME, "mat-grid-list")
        order = "Locators." + order_item
        order = order_item.replace("\"", "")
        driver.find_element_by_xpath(Locators.egg_fruit_juice).click()

