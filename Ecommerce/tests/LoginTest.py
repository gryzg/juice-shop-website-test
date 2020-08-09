import unittest
import time
import HtmlTestRunner

from selenium import webdriver

from resources.environment_variables import EnvVariables
from resources.locators import Locators
from resources.BasePage import BasePage
from resources.LoginPage import LoginPage
from resources.HomePage import HomePage


class LoginTest(unittest.TestCase):
    invalid_login_msg = 'Invalid email or password.'

    def setUp(self):
        self.driver = webdriver.Chrome(EnvVariables.CHROME_DRIVER_PATH)
        self.driver.get(EnvVariables.WEBSITE_URL)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(EnvVariables.TIMEOUT)


    def tc001_login_successful(self):
        driver = self.driver
        self.assertIn("OWASP Juice Shop", driver.title)

        LoginPage.handle_login_popups(driver)
        LoginPage.login_to_account(driver, EnvVariables.USERNAME, EnvVariables.PASSWORD)
        account_logged_in = HomePage.get_logged_in_account(driver)
        BasePage.assert_element_text(EnvVariables.USERNAME, account_logged_in)
        print ("Login successful.")

    def tc002_login_invalid_password(self):
        driver = self.driver
        LoginPage.handle_login_popups(driver)
        invalid_password = 'Abcd1234'
        LoginPage.login_to_account(driver, EnvVariables.USERNAME, invalid_password)
        login_msg = driver.find_element_by_xpath(Locators.LOGIN_MSG)
        actual_login_msg = login_msg.text
        #assert (driver, LoginTest.invalid_login_msg, actual_login_msg, "Invalid login")
        assert LoginTest.invalid_login_msg == actual_login_msg

    def tc003_login_invalid_username(self):
        driver = self.driver
        LoginPage.handle_login_popups(driver)
        invalid_username = 'testt@test.com'
        LoginPage.login_to_account(driver, invalid_username, EnvVariables.PASSWORD)
        login_msg = driver.find_element_by_xpath(Locators.LOGIN_MSG)
        actual_login_msg = login_msg.text
        assert LoginTest.invalid_login_msg == actual_login_msg
        #assert (driver, LoginTest.invalid_login_msg, actual_login_msg, "Invalid login")

    #def tc004_forgot_password(self):

    def tearDown(self):
        time.sleep(4)
        self.driver.quit()
        print ("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports'))