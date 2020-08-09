from selenium.webdriver.common.by import By

from resources.utilities import Utilities


class Locators():

    # *** Landing Page Locators ***
    COOKIE_MESSAGE = "//div/a[@aria-label='dismiss cookie message']"
    CLOSE_WELCOME_BANNER = "//*[@aria-label='Close Welcome Banner']"

    # *** Login Page Locators ***
    NAV_BAR_ACCOUNT_BTN = "navbarAccount"
    NAV_BAR_LOGIN_BTN = "navbarLoginButton"
    EMAIL = "email"
    PASSWORD = "password"
    LOGIN_BTN = "loginButton"
    ACCOUNT_LOGGED_IN = "//*[@id='mat-menu-panel-0']/div/button[@aria-label='Go to user profile']/span"
    LOGIN_MSG = "//app-login/div/mat-card/div[@class='error ng-star-inserted']"


    # *** Home Page Locators ***
    #Add To Basket Buttons
    #Refactor this: Create Python Dictionary (key=item, pair=indices to retrieve locators)
    apple_juice = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[1])//button"
    apple_pomace = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[2])//button"
    banana_juice = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[3])//button"
    carrot_juice = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[4])//button"
    egg_fruit_juice = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[5])//button"
    fruit_press = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[6])//button"
    green_smoothie = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[7])//button"
    juice_shop_trading_card_common = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[8])//button"
    juice_shop_trading_card_rare = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[9])//button"
    juice_shop_art_work = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[10])//button"
    lemon_juice = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[11])//button"
    melon_bike = "((//mat-grid-tile[@class='mat-grid-tile ng-star-inserted'])[12])//button"

    #Paginator Buttons
        #page_drop_down_menu
        #previous_page_btn
        #next_page_btn


    # *** Your Basket Locators ***
    YOUR_BASKET_BTN = "//button[@aria-label='Show the shopping cart']"
    YOUR_BASKET_ITEM = "//app-purchase-basket/mat-table/mat-row/mat-cell[2]"
    YOUR_BASKET_ITEM_QTY = "//app-purchase-basket/mat-table/mat-row/mat-cell[3]/span"

    # *** Checkout Locators ***
    CHECKOUT_BTN = "checkoutButton"
    ADDRESS_RADIO_BTN_1 = "mat-radio-40"
    ADDRESS_RADIO_BTN_2 = "mat-radio-41"
    ADDRESS_RADIO_BTN_3 = "mat-radio-42"
    DELIVERY_BTN = "//button[@aria-label='Proceed to payment selection']"
    DELIVERY_ONE_DAY_RADIO_BTN = "mat-radio-43"
    DELIVERY_FAST_RADIO_BTN = "mat-radio-43"
    DELIVERY_STANDARD_RADIO_BTN = "mat-radio-43"

    CONTINUE_TO_PAYMENT_BTN = "//button[@aria-label='Proceed to delivery method selection']"

    # *** Payment Locators ***
    CREDIT_CARD_RADIO_BTN_1 = "mat-radio-46"
    CREDIT_CARD_RADIO_BTN_2 = "mat-radio-47"
    CONTINUE_TO_REVIEW_BTN = "//button[@aria-label='Proceed to review']"
    FINAL_CHECKOUT_BTN = "//button[@id='checkoutButton' and @aria-label='Complete your purchase']"


