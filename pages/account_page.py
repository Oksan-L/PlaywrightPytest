from .base_page import BasePage

class AccountPage(BasePage):

    account_created = "b:has-text('Account Created!')"
    continue_btn = "a[data-qa='continue-button']"
    logged_in_as = "a:has-text('Logged in as')"
    delete_account_btn = "a[href='/delete_account']"
    account_deleted = "b:has-text('Account Deleted!')"

    def verify_account_created(self):
        self.expect_visible(self.account_created)

    def click_continue(self):
        self.click(self.continue_btn)

    def verify_logged_in(self):
        self.expect_visible(self.logged_in_as)

    def delete_account(self):
        self.click(self.delete_account_btn)

    def verify_deleted(self):
        self.expect_visible(self.account_deleted)

    def click_continue_after_delete(self):
        self.click(self.continue_btn)