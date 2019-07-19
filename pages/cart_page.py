from base_page import BasePage
from locators import CartPageLocators

class CartPage(BasePage):
    def should_see_message_no_products_in_the_cart(self):
        assert self.is_element_present(*CartPageLocators.NO_ITEM_IN_CART_MESSAGE), \
        "There are no messages about the absence of goods in the basket, it should be"

    def should_see_no_products_in_the_cart(self):
        assert self.is_not_element_present(*CartPageLocators.ITEM_IN_CART_MESSAGE), \
        "The item in the basket is, should not be"
