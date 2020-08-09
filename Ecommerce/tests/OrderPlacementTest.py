import unittest
import time
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#Hover
from selenium.webdriver.common.action_chains import ActionChains

from resources.environment_variables import EnvVariables
from resources.locators import Locators
from resources.BasePage import BasePage
from resources.LoginPage import LoginPage
from resources.HomePage import HomePage
from resources.YourBasketPage import YourBasketPage

class OrderPlacementTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(EnvVariables.CHROME_DRIVER_PATH)
        cls.driver.get(EnvVariables.WEBSITE_URL)
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(EnvVariables.TIMEOUT)

    def test_order_successful(self):
        """Verify that order is placed for an existing customer when payment is successful"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        self.assertIn("OWASP Juice Shop", driver.title)

        LoginPage.handle_login_popups(driver)
        LoginPage.login_to_account(driver, EnvVariables.USERNAME, EnvVariables.PASSWORD)

        #Place single order
        order_item = "egg_fruit_juice"
        HomePage.add_to_cart(driver, order_item)
        #Assert popup placed order should come up
        time.sleep(4)

        #Review Basket Items
        YourBasketPage.review_basket_items(driver)
        basket_items = YourBasketPage.review_basket_items(driver)
        #Assert that <Item Placed> is shown in Cart with correct quantity and amount

        #Checkout
        BasePage.element_is_visible(driver, By.ID, Locators.CHECKOUT_BTN)
        driver.find_element_by_id(Locators.CHECKOUT_BTN).click()

        #Select existing address
        BasePage.element_is_visible(driver, By.ID, Locators.ADDRESS_RADIO_BTN_3)
        driver.find_element_by_id(Locators.ADDRESS_RADIO_BTN_3).click()

        #Go to Delivery
        BasePage.element_is_visible(driver, By.XPATH, Locators.DELIVERY_BTN)
        driver.find_element_by_xpath(Locators.DELIVERY_BTN).click

        #Select Delivery Timeframe
        BasePage.element_is_visible(driver, By.ID, Locators.DELIVERY_ONE_DAY_RADIO_BTN)
        driver.find_element_by_xpath(Locators.DELIVERY_ONE_DAY_RADIO_BTN).click
        driver.find_element_by_xpath(Locators.CONTINUE_TO_PAYMENT_BTN).click()

        #Credit Card Payment
        driver.find_element_by_id(Locators.CREDIT_CARD_RADIO_BTN_1).click()
        driver.find_element_by_xpath(Locators.CONTINUE_TO_REVIEW_BTN).click()

        #Assert order summary and amount
        driver.find_element_by_xpath(Locators.FINAL_CHECKOUT_BTN).click()
        #Assert "Thank you for your purchase"


    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.get_screenshot_as_file("order-placement-test-screenshot.png")
        cls.driver.quit()
        #cls.manage().deleteAllCookies()
        print ("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))

