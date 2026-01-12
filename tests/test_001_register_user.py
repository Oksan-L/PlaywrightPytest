import allure
from faker import Faker
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_page import AccountPage

faker = Faker()

@allure.title("001-Register User")
def test_register_user(page):

    name = faker.first_name()
    email = faker.email()
    password = faker.password()
    fname = faker.first_name()
    lname = faker.last_name()
    address = faker.address().replace("\n", " ")
    state = "CA"
    city = "Los Angeles"
    zipcode = "90001"
    mobile = faker.msisdn()

    base_url = "http://automationexercise.com"

    # Pages
    home = HomePage(page)
    login = LoginPage(page)
    signup = SignupPage(page)
    account = AccountPage(page)

    # Steps
    home.open(base_url)
    home.verify_home_visible()
    home.go_to_signup_login()

    login.verify_new_user_title()
    login.enter_signup_data(name, email)

    signup.verify_enter_account_info()
    signup.fill_basic_info(password)
    signup.fill_address(fname, lname, address, state, city, zipcode, mobile)
    signup.click_create_account()

    account.verify_account_created()
    account.click_continue()
    account.verify_logged_in()

    account.delete_account()
    account.verify_deleted()
    account.click_continue_after_delete()
