from playwright.sync_api import Page, expect

class AdminPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_admin(self):
        self.page.get_by_role("link", name="Admin").click()
        expect(self.page.get_by_role("heading", name="Admin")).to_be_visible(timeout=20000)

    def _select_dropdown_option(self, dropdown_label: str, option_text: str):
        self.page.locator(f"//label[text()='{dropdown_label}']/../following-sibling::div//div[contains(@class,'oxd-select-text')]").click()
        self.page.get_by_role("option", name=option_text).click()

    def _fill_employee_name(self):
        employee_input = self.page.get_by_placeholder("Type for hints...")
        employee_input.fill("a")
        first_option = self.page.locator(".oxd-autocomplete-dropdown .oxd-autocomplete-option").first
        expect(first_option).to_be_visible(timeout=15000)
        first_option.click()

    def add_user(self, role: str, status: str, username: str, password: str):
        self.page.get_by_role("button", name="Add").click()
        expect(self.page.get_by_role("heading", name="Add User")).to_be_visible(timeout=15000)

        self._select_dropdown_option("User Role", role)
        self._fill_employee_name()
        self._select_dropdown_option("Status", status)

        self.page.locator("//label[text()='Username']/../following-sibling::div/input").fill(username)
        self.page.locator("//label[text()='Password']/../following-sibling::div/input").fill(password)
        self.page.locator("//label[text()='Confirm Password']/../following-sibling::div/input").fill(password)

        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Successfully Saved")).to_be_visible(timeout=20000)
        expect(self.page.get_by_role("heading", name="System Users")).to_be_visible(timeout=20000)

    def search_user(self, username: str):
        self.page.locator("//label[text()='Username']/../following-sibling::div/input").fill(username)
        self.page.get_by_role("button", name="Search").click()
        expect(self.page.locator(".orangehrm-container")).to_be_visible(timeout=15000)
        expect(self.page.get_by_text(username)).to_be_visible(timeout=20000)

    def reset_search(self):
        self.page.get_by_role("button", name="Reset").click()
        expect(self.page.get_by_role("heading", name="System Users")).to_be_visible(timeout=15000)

    def open_first_user_for_edit(self):
        self.page.locator(".oxd-table-cell-actions button").nth(1).click()
        expect(self.page.get_by_role("heading", name="Edit User")).to_be_visible(timeout=15000)

    def save_user(self):
        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Successfully Updated")).to_be_visible(timeout=20000)

    def edit_role(self, new_role: str):
        self.open_first_user_for_edit()
        self._select_dropdown_option("User Role", new_role)
        self.save_user()

    def edit_status(self, new_status: str):
        self.open_first_user_for_edit()
        self._select_dropdown_option("Status", new_status)
        self.save_user()

    def edit_username(self, new_username: str):
        self.open_first_user_for_edit()
        username_input = self.page.locator("//label[text()='Username']/../following-sibling::div/input")
        username_input.fill(new_username)
        self.save_user()

    def change_password(self, new_password: str):
        self.open_first_user_for_edit()
        self.page.locator("label:has-text('Change Password')").click()
        self.page.locator("//label[text()='Password']/../following-sibling::div/input").fill(new_password)
        self.page.locator("//label[text()='Confirm Password']/../following-sibling::div/input").fill(new_password)
        self.save_user()

    def validate_user_in_result(self, username: str, expected_status: str = None):
        expect(self.page.get_by_text(username)).to_be_visible(timeout=15000)
        if expected_status:
            expect(self.page.get_by_text(expected_status).first).to_be_visible(timeout=15000)

    def delete_user(self):
        delete_buttons = self.page.locator(".oxd-table-cell-actions button")
        delete_buttons.first.click()
        expect(self.page.get_by_role("button", name="Yes, Delete")).to_be_visible(timeout=10000)
        self.page.get_by_role("button", name="Yes, Delete").click()
        expect(self.page.get_by_text("Successfully Deleted")).to_be_visible(timeout=20000)

    def validate_user_not_found(self, username: str):
        self.page.locator("//label[text()='Username']/../following-sibling::div/input").fill(username)
        self.page.get_by_role("button", name="Search").click()
        expect(self.page.get_by_text("No Records Found")).to_be_visible(timeout=20000)
