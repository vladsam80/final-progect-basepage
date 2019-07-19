#pytest -s -v --tb=line --language=en test_main_page.py
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest

LINK = "http://selenium1py.pythonanywhere.com"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.cart_see
def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_see_message_no_products_in_the_cart()
    cart_page.should_see_no_products_in_the_cart()
