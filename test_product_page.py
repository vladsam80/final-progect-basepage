from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_cart(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_the_cart()
    page.solve_quiz_and_get_code()
