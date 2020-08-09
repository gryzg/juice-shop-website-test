# --- Login Page Methods
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from resources.BasePage import BasePage
from resources.environment_variables import EnvVariables
from resources.locators import Locators

class LoginPage(BasePage):
    def __init__(self, driver):
        driver = self.driver

    def handle_login_popups(driver):
        BasePage.element_is_visible(driver, By.XPATH, Locators.COOKIE_MESSAGE)
        driver.find_element_by_xpath(Locators.COOKIE_MESSAGE).click()

        BasePage.element_is_visible(driver, By.XPATH, Locators.CLOSE_WELCOME_BANNER)
        driver.find_element_by_xpath(Locators.CLOSE_WELCOME_BANNER).click()

    def login_to_account(driver, username, password):
        account_btn = driver.find_element_by_id(Locators.NAV_BAR_ACCOUNT_BTN)
        account_btn.click()
        driver.find_element_by_id(Locators.NAV_BAR_LOGIN_BTN).click()

        BasePage.element_is_visible(driver, By.ID, Locators.EMAIL)
        driver.find_element_by_id(Locators.EMAIL).send_keys(username)
        driver.find_element_by_id(Locators.PASSWORD).send_keys(password)
        driver.find_element_by_id(Locators.LOGIN_BTN).click()