from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        auth = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        auth.send_keys(email)
        auth = self.browser.find_element(*LoginPageLocators.PASSWD_FORM_1)
        auth.send_keys(password)
        auth = self.browser.find_element(*LoginPageLocators.PASSWD_FORM_2)
        auth.send_keys(password)
        auth = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        auth.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is no login in the link"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
