from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
import pytest
import time

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", \
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", \
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", \
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", \
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", \
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", \
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", \
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", \
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", \
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_the_cart()
    page.solve_quiz_and_get_code()
    page.should_be_success_of_addition_message()

LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.negative_checks
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_the_cart()
    page.should_not_be_success_message()

@pytest.mark.negative_checks
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.negative_checks
def test_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_the_cart()
    page.should_be_dissapeared()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_see_message_no_products_in_the_cart()
    cart_page.should_see_no_products_in_the_cart()

@pytest.mark.user_add
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@yandex.org"
        password = email
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        self.browser = browser

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self):
        page = ProductPage(self.browser, LINK)
        page.open()
        page.add_to_the_cart()
        page.should_be_success_of_addition_message()

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, LINK)
        page.open()
        page.should_not_be_success_message()
