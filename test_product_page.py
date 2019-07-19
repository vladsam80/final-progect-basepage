#pytest -v --tb=line test_product_page.py
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
# import pytest
##from time import sleep

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", \
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", \
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", \
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", \
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", \
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", \
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", \
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", \
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", \
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_cart(browser, link):
    # page = ProductPage(browser, link)
    # page.open()
    # page.add_to_the_cart()
    # page.solve_quiz_and_get_code()
    ##sleep(10)
    # page.should_be_success_of_addition_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
