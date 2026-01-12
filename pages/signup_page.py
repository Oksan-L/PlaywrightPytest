from .base_page import BasePage

class SignupPage(BasePage):

    enter_account_info_title = "b:has-text('Enter Account Information')"
    title_mr = "#id_gender1"
    password_input = "#password"
    days = "#days"
    months = "#months"
    years = "#years"

    newsletter_checkbox = "#newsletter"
    offers_checkbox = "#optin"

    first_name = "#first_name"
    last_name = "#last_name"
    address1 = "#address1"
    country = "#country"
    state = "#state"
    city = "#city"
    zipcode = "#zipcode"
    mobile_number = "#mobile_number"

    create_account_btn = "button[data-qa='create-account']"

    def verify_enter_account_info(self):
        self.expect_visible(self.enter_account_info_title)

    def fill_basic_info(self, password):
        self.click(self.title_mr)
        self.fill(self.password_input, password)
        self.page.select_option(self.days, "10")
        self.page.select_option(self.months, "5")
        self.page.select_option(self.years, "1995")
        self.click(self.newsletter_checkbox)
        self.click(self.offers_checkbox)

    def fill_address(self, fname, lname, address, state, city, zipc, phone):
        self.fill(self.first_name, fname)
        self.fill(self.last_name, lname)
        self.fill(self.address1, address)
        self.fill(self.state, state)
        self.fill(self.city, city)
        self.fill(self.zipcode, zipc)
        self.fill(self.mobile_number, phone)

    def click_create_account(self):
        self.click(self.create_account_btn)
