from playwright.sync_api import Page, expect
from utils.test_data import BASE_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto(BASE_URL, wait_until="domcontentloaded")
        expect(self.username_input).to_be_visible(timeout=15000)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible(timeout=20000)
