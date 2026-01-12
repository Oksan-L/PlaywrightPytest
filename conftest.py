import pytest
import allure

@pytest.fixture(autouse=True)
def screenshot_on_failure(page):
    yield
    # Make screenshot automatically on test failure
    # Or at the end of each test
    allure.attach(
        page.screenshot(full_page=True),
        name="Final Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
