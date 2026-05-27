from datetime import datetime

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
ADMIN_USERNAME = "Admin"
ADMIN_PASSWORD = "admin123"

PASSWORD = "Test@12345"
UPDATED_PASSWORD = "Test@54321"

def unique_username(prefix: str = "accu_test") -> str:
    return f"{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
