from playwright.sync_api import Page, expect
import allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        with allure.step(f"Open URL: {url}"):
            self.page.goto(url)

    def click(self, locator):
        with allure.step(f"Click element: {locator}"):
            self.page.locator(locator).click()

    def fill(self, locator, value):
        with allure.step(f"Fill {locator} with {value}"):
            self.page.locator(locator).fill(value)

    def expect_visible(self, locator):
        with allure.step(f"Verify visible: {locator}"):
            expect(self.page.locator(locator)).to_be_visible()
    