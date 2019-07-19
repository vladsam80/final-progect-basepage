from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "header a.btn.btn-default")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    ADD_TO_THE_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_MESSAGE_OF_SUCCESFUL_ADDITION = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner")

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class CartPageLocators(object):
    ITEM_IN_CART_MESSAGE = (By.CSS_SELECTOR, ".basket-title .col-sm-6")
    NO_ITEM_IN_CART_MESSAGE = (By.CSS_SELECTOR, ".content #content_inner > p")
