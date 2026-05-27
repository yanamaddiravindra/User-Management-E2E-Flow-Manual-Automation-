import pytest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.test_data import (
    ADMIN_USERNAME,
    ADMIN_PASSWORD,
    PASSWORD,
    UPDATED_PASSWORD,
    unique_username,
)

@pytest.fixture(scope="session")
def user_data():
    username = unique_username()
    return {
        "username": username,
        "updated_username": username.replace("accu_test", "accu_updated"),
        "role": "ESS",
        "updated_role": "Admin",
        "status": "Enabled",
        "updated_status": "Disabled",
    }

@pytest.fixture(scope="session")
def logged_in_page(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    yield page
    page.close()

@pytest.fixture(scope="session")
def admin_page(logged_in_page):
    admin = AdminPage(logged_in_page)
    admin.navigate_to_admin()
    return admin

@pytest.mark.e2e
def test_01_navigate_to_admin_module(admin_page):
    admin_page.page.get_by_role("heading", name="System Users").wait_for(timeout=15000)

@pytest.mark.e2e
def test_02_add_new_user(admin_page, user_data):
    admin_page.add_user(
        role=user_data["role"],
        status=user_data["status"],
        username=user_data["username"],
        password=PASSWORD,
    )

@pytest.mark.e2e
def test_03_search_newly_created_user(admin_page, user_data):
    admin_page.search_user(user_data["username"])
    admin_page.validate_user_in_result(user_data["username"], user_data["status"])

@pytest.mark.e2e
def test_04_edit_user_role(admin_page, user_data):
    admin_page.search_user(user_data["username"])
    admin_page.edit_role(user_data["updated_role"])
    admin_page.search_user(user_data["username"])
    admin_page.validate_user_in_result(user_data["username"])

@pytest.mark.e2e
def test_05_edit_user_status(admin_page, user_data):
    admin_page.search_user(user_data["username"])
    admin_page.edit_status(user_data["updated_status"])
    admin_page.search_user(user_data["username"])
    admin_page.validate_user_in_result(user_data["username"], user_data["updated_status"])

@pytest.mark.e2e
def test_06_edit_username(admin_page, user_data):
    admin_page.search_user(user_data["username"])
    admin_page.edit_username(user_data["updated_username"])
    admin_page.search_user(user_data["updated_username"])
    admin_page.validate_user_in_result(user_data["updated_username"])

@pytest.mark.e2e
def test_07_change_password(admin_page, user_data):
    admin_page.search_user(user_data["updated_username"])
    admin_page.change_password(UPDATED_PASSWORD)
    admin_page.search_user(user_data["updated_username"])
    admin_page.validate_user_in_result(user_data["updated_username"])

@pytest.mark.e2e
def test_08_validate_updated_details(admin_page, user_data):
    admin_page.search_user(user_data["updated_username"])
    admin_page.validate_user_in_result(user_data["updated_username"], user_data["updated_status"])

@pytest.mark.e2e
def test_09_delete_user(admin_page, user_data):
    admin_page.search_user(user_data["updated_username"])
    admin_page.delete_user()

@pytest.mark.e2e
def test_10_validate_deleted_user_not_searchable(admin_page, user_data):
    admin_page.validate_user_not_found(user_data["updated_username"])
