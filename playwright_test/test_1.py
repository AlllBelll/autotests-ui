"""
Задача:
1. Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login
2. Проверить наличие элементов: "Email", "Password", "Login"
3. Нажать на ссылку "Registration", после чего произойдет редирект на страницу Registration
4. Проверить наличие элементов: "Email", "Password", "Registration"
"""

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browse = playwright.chromium.launch(headless=False)
    page = browse.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    email_input = page.get_by_test_id("login-form-email-input").locator("input")
    expect(email_input).to_be_visible()

    password_input = page.get_by_test_id("login-form-password-input").locator("input")
    expect(password_input).to_be_visible()

    login_button = page.get_by_test_id("login-page-login-button")
    expect(login_button).to_be_visible()

    registration_button = page.get_by_test_id("login-page-registration-link")
    registration_button.click()

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    expect(email_input).to_be_visible()

    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    expect(password_input).to_be_visible()

    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_visible()



