"""
Задача:
 - Откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
 - Заполнит поле "Email" значением "user.name@gmail.com"
 - Заполнит поле "Username" значением "username"
 - Заполнит поле "Password" значением "password"
 - Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard"
 - Проверит, что на странице "Dashboard" отображается заголовок "Dashboard"
"""

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as palywright:
    browser = palywright.chromium.launch()
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("test_user@testpage.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill("test_user")

    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("Test_pass123!")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_have_text("Dashboard")