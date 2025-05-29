import time
def login(page, email, password):

    email_input = page.locator('input').nth(0)
    email_input.wait_for(state="visible")
    email_input.fill(email)

    page.get_by_role("button", name="Next").click()

    password_input = page.locator('input').nth(1)
    password_input.wait_for(state="visible")
    password_input.fill(password)
    while password_input.input_value() != password:
        time.sleep(1)

    sign_in_button = page.get_by_role("button", name="Sign in")
    sign_in_button.wait_for(state="visible")
    sign_in_button.click()

    yes_button = page.get_by_text("Yes", exact=True).nth(0)
    yes_button.wait_for(state="visible")
    yes_button.click()