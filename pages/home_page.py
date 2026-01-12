from .base_page import BasePage

class HomePage(BasePage):

    signup_login_btn = "a[href='/login']"
    homepage_slider = "#slider"

    def verify_home_visible(self):
        self.expect_visible(self.homepage_slider)

    def go_to_signup_login(self):
        self.click(self.signup_login_btn)
