from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_the_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_THE_BASKET_BUTTON).click()
		
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_addition_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_OF_SUCCESFUL_ADDITION).text

    def should_be_success_of_addition_message(self):
        assert self.get_addition_message() == self.get_product_name(), "Error. Item does not match."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_be_dissapeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should has dissapeared"