#pytest -v --tb=line --language=en test_negative_checks.py
from .pages.product_page import ProductPage

LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"

def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_the_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_cart(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_the_cart()
    page.should_be_dissapeared()