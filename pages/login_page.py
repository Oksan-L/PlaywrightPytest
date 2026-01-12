from .base_page import BasePage

class LoginPage(BasePage):

    new_user_title = "h2:has-text('New User Signup!')"
    name_input = "input[data-qa='signup-name']"
    email_input = "input[data-qa='signup-email']"
    signup_btn = "button[data-qa='signup-button']"

    def verify_new_user_title(self):
        self.expect_visible(self.new_user_title)

    def enter_signup_data(self, name, email):
        self.fill(self.name_input, name)
        self.fill(self.email_input, email)
        self.click(self.signup_btn)
