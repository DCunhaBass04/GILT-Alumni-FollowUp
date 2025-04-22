import time
from playwright.sync_api import sync_playwright
import configparser
from login import login
import sys

if __name__ == "__main__":
  state = sys.argv[1]   # "True" se for para abrir o Forms
                        # "False" se for para fechar o Forms

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, slow_mo=100) # headless=True quando usar na VM
                                                            # headless=False para demonstrar

    config = configparser.ConfigParser()
    config.read('conf.cfg')
    url = config['START']['forms_admin_url']

    config.read('credentials.cfg')
    email = config['CREDENTIALS']['email']
    password = config['CREDENTIALS']['password']

    page = browser.new_page()
    page.goto(url)

    login(page, email, password)

    page.locator('[aria-label="Settings"]' # Ou "Definições" em PT
                ).wait_for(state="visible")
    page.locator('[aria-label="Settings"]').click()

    checkbox = page.get_by_role("checkbox", name="Accept responses")
    checkbox.wait_for(state="visible")
    if checkbox.get_attribute("aria-checked") != str(state).lower():
        checkbox.click()

    time.sleep(10) # Espera necessária para o Forms armazenar a alteração
