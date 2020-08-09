from selenium.webdriver.common.by import By

from resources.locators import Locators
from resources.BasePage import BasePage


class YourBasketPage(BasePage):

    def __init__(self, driver):
        driver = self.driver

    def review_basket_items(driver):
        BasePage.element_is_visible(driver, By.XPATH, Locators.YOUR_BASKET_BTN)
        driver.find_element_by_xpath(Locators.YOUR_BASKET_BTN).click()
        BasePage.element_is_visible(driver, By.XPATH, Locators.YOUR_BASKET_ITEM)

        basket_item = driver.find_element_by_xpath(Locators.YOUR_BASKET_ITEM).text
        basket_item_qty = driver.find_element_by_xpath(Locators.YOUR_BASKET_ITEM_QTY).text

        return basket_item, basket_item_qty