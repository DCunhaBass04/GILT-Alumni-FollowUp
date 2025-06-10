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
        self.url_convite = config['AUTOMATE']['convite_url']
        self.url_lembrete = config['AUTOMATE']['lembrete_url']
        self.url_fim = config['AUTOMATE']['fim_url']

    def run(self, iso_date_beginning, iso_date_reminder, iso_date_end):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, slow_mo=100)  # Usa headless=False para debug
            page = browser.new_page()
            login_tool = LoginMicrosoft()

            try:
                # CONVITE
                page.goto(self.url_convite)
                login_tool.login(page, self.email, self.password)
                time.sleep(10)
                page.get_by_text("Aceitar").click()
                self.ensure_classic_designer(page)
                self.change_date_recurrence(page, iso_date_beginning)

                # LEMBRETE
                page.goto(self.url_lembrete)
                self.ensure_classic_designer(page)
                self.change_date_recurrence(page, iso_date_reminder)

                # FIM
                page.goto(self.url_fim)
                self.ensure_classic_designer(page)
                self.change_date_recurrence(page, iso_date_end)

                browser.close()
                return "Data alterada com sucesso."

            except Exception as e:
                page.screenshot(path="Error.png")
                print(e)
                browser.close()
                return f"Erro ao alterar data: {str(e)}"
            
    def fechar_modal_feedback(self, page):
        try:
            print("A verificar presença do modal de feedback...")

            close_btn = page.locator('button[data-automation-id="sidePanelCloseButton"]')
            close_btn.wait_for(state="visible", timeout=10000)

            print("Botão de fechar do side panel encontrado — a fechar.")
            close_btn.click()

            page.wait_for_selector('.ms-Overlay', state='detached', timeout=10000)
            print("Side panel fechado com sucesso.")

        except Exception as e:
            print("Erro ao fechar modal de feedback:", e)



    def ensure_classic_designer(self, page):
        try:
            button = page.locator('button[role="switch"][aria-label="Novo estruturador"]')
            button.wait_for(timeout=10000)

            if button.get_attribute("aria-checked") == "true":
                print("Novo estruturador ativado — será desmarcado.")
                button.click()
                try:
                    page.get_by_text("Mudar sem guardar").click()
                except Exception as e:
                    print(e)

                self.fechar_modal_feedback(page)
                page.wait_for_selector('.ms-Overlay', state='detached', timeout=10000)
            else:
                print("Novo estruturador já está desativado.")

        except Exception as e:
            print("Erro ao verificar ou desativar Novo estruturador:", e)



    def change_date_recurrence(self, page, date):
        time.sleep(5)
        page.wait_for_selector('.ms-Overlay', state='detached', timeout=10000)  # Aguarda a overlay desaparecer

        page.get_by_text("Recurrence").first.click()
        time.sleep(2)

        page.get_by_text("Mostrar opções avançadas").first.click()
        time.sleep(2)

        campo = page.get_by_label("Hora de início")
        campo.wait_for(state="visible", timeout=10000)
        campo.fill("")
        campo.type(date)
        campo.press("Tab")

        page.eval_on_selector('button[data-automation-id="action_save"]', 'el => el.click()')
        page.wait_for_load_state("networkidle")
        time.sleep(10)

