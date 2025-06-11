import time
from playwright.sync_api import sync_playwright
import configparser
from automation.login import LoginMicrosoft
import os

def get_settings():
    try:
        from django.conf import settings
        _ = settings.CONFIG_PATH
        return settings
    except Exception:
        class SimpleSettings:
            CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../conf.cfg'))
            CREDENTIALS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../credentials.cfg'))
            EXCEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../TeamsDrive/Respostas.xlsx'))
        return SimpleSettings()

settings = get_settings()

def toggle_forms(page, url, state: bool):
    page.goto(url)
    page.locator('[aria-label="Settings"]').wait_for(state="visible")
    page.locator('[aria-label="Settings"]').click()

    checkbox = page.get_by_role("checkbox", name="Accept responses")
    checkbox.wait_for(state="visible")

    if checkbox.get_attribute("aria-checked") != str(state).lower():
        checkbox.click()

    time.sleep(10)  # Espera necessária para o Forms armazenar a alteração

def run(state: bool):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=100)

        config = configparser.ConfigParser()
        config.read(settings.CONFIG_PATH)
        url1 = config['START']['forms_admin_url']
        url2 = config['START']['first_forms_admin_url']

        config.read(settings.CREDENTIALS_PATH)
        email = config['CREDENTIALS']['email']
        password = config['CREDENTIALS']['password']

        page = browser.new_page()
        page.goto(url1)

        try:
            login_tool = LoginMicrosoft()
            login_tool.login(page, email, password)

            toggle_forms(page, url1, state)
            toggle_forms(page, url2, state)

            browser.close()
            return "Operação terminada com sucesso"

        except Exception as e:
            page.screenshot(path="Error.png")
            browser.close()
            return f"Erro ao executar operação: {str(e)}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python toggle_forms.py True|False")
        sys.exit(1)

    arg = sys.argv[1].strip().lower()
    if arg not in ("true", "false"):
        print("Erro: argumento deve ser 'True' ou 'False'")
        sys.exit(1)

    state_bool = arg == "true"
    run(state_bool)