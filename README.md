# AccuKnox User Management Tests

Practical assessment automation for the OrangeHRM User Management E2E flow.

## Application Under Test

URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Credentials:
- Username: `Admin`
- Password: `admin123`

## Tech Stack

- Python
- Pytest
- Playwright
- Page Object Model

## Playwright Version Used

`playwright==1.54.0`

## Project Structure

```text
AccuKnox-user-management-tests/
├── pages/
│   ├── login_page.py
│   └── admin_page.py
├── tests/
│   └── test_user_management.py
├── utils/
│   └── test_data.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Setup Steps

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/AccuKnox-user-management-tests.git
cd AccuKnox-user-management-tests
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:

```bash
playwright install
```

## How to Run Test Cases

Run all tests:

```bash
pytest
```

Run in headed mode:

```bash
pytest --headed
```

Run in Chromium only:

```bash
pytest --browser chromium
```

Generate HTML report/trace if needed:

```bash
pytest --tracing on
```

## Test Scenarios Covered

1. Login and navigate to Admin module
2. Add a new user
3. Search newly created user
4. Edit user role
5. Edit user status
6. Edit username
7. Change password
8. Validate updated details
9. Delete user
10. Validate deleted user is not searchable

## Important Notes

- OrangeHRM demo data can reset or change. The script selects an existing employee from the dropdown dynamically.
- Username is generated using timestamp to avoid duplicate username errors.
- If employee dropdown does not load immediately, rerun the test or increase timeout.
- The public demo site may be slow, so explicit waits are added for important elements.
