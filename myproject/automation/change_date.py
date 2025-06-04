from playwright.sync_api import sync_playwright
import configparser
import time

from automation.login import LoginMicrosoft

class DateChanger:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('../credentials.cfg')
        self.email = config['CREDENTIALS']['email']
        self.password = config['CREDENTIALS']['password']

        config.read('../conf.cfg')
        self.url = config['AUTOMATE']['convite_url']

    def run(self, iso_date):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, slow_mo=100)
            page = browser.new_page()
            print(self.url)
            page.goto(self.url)

            try:
                login_tool = LoginMicrosoft()
                login_tool.login(page, self.email, self.password)
                self.change_date_recurrence(page, self.url, iso_date)
                page.screenshot(path="screenshot.png")
                browser.close()
                return "Data alterada com sucesso."

            except Exception as e:
                page.screenshot(path="Error.png")
                browser.close()
                return f"Erro ao alterar data: {str(e)}"

    def change_date_recurrence(self, page, url, date):
        page.goto(url)
        time.sleep(20)

        page.get_by_text("Recurrence").nth(0).click()
        time.sleep(2)

        page.get_by_text("Mostrar opções avançadas").nth(0).click()
        time.sleep(2)

        campo = page.get_by_label("Hora de início")
        campo.wait_for(state="visible", timeout=10000)
        campo.fill(date)

        page.get_by_role("button", name="Guardar").click()
        time.sleep(5)
