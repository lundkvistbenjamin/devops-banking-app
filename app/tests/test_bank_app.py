import pytest
from app.bank_app import BankApp

@pytest.fixture
def bank_app():
    return BankApp()

def test_login_success(bank_app):
    result = bank_app.login("user1", "pass1")
    assert result == "Login successful"
    assert bank_app.current_user["balance"] == 1000

def test_login_failure(bank_app):
    result = bank_app.login("user1", "wrongpass")
    assert result == "Invalid username or password"
    assert bank_app.current_user is None

def test_show_account_info(bank_app):
    bank_app.login("user1", "pass1")
    account_info = bank_app.show_account_info()
    assert account_info["balance"] == 1000
    assert account_info["account_number"] == "111-111-111"

def test_logout(bank_app):
    bank_app.login("user1", "pass1")
    result = bank_app.logout()
    assert result == "Logged out successfully"
    assert bank_app.current_user is None

def test_view_balance(bank_app):
    bank_app.login("user1", "pass1")
    account_info = bank_app.show_account_info()
    assert account_info["balance"] == 1000

def test_view_account_number(bank_app):
    bank_app.login("user1", "pass1")
    account_info = bank_app.show_account_info()
    assert account_info["account_number"] == "111-111-111"
