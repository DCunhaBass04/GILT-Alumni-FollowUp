from playwright.sync_api import sync_playwright
import configparser

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

    page.locator('input').nth(0).wait_for(state="visible")
    page.fill('input >> nth=0', email) 
    page.get_by_role("button", name="Next" # ou "Seguinte" em PT
                     ).click()

    page.locator('input').nth(1).wait_for(state="visible")
    page.fill('input >> nth=1', password)
    page.get_by_role("button", name="Sign in" # ou "Iniciar Sessão" em PT
                     ).click()

    page.get_by_text("Yes" # ou "Sim" em PT
                     , exact=True).nth(0).wait_for(state="visible")
    page.get_by_text("Yes", exact=True).nth(0).click()

    page.locator(".dropdown-placeholder-arrow").wait_for(state='visible')
    page.locator(".dropdown-placeholder-arrow").click(force=True)
    page.locator('[aria-label="Get Pre-filled URL"]' # Ou "Obter URL Pré-preenchido" em PT
                 ).wait_for(state="visible")
    page.locator('[aria-label="Get Pre-filled URL"]').click()

    # Preencher campos
    page.locator('input').nth(0).wait_for(state="visible")
    page.fill('input >> nth=0', "diogo10072004@isep.ipp.pt")
    page.fill('input >> nth=1', "Diogo Teste Playwright")
    page.get_by_text("Sim", exact=True).nth(0).click()

    
    page.get_by_role("button", name="Get Prefilled Link" # ou "Obter Ligação Pré-Preenchida" em PT
                     ).click()


    page.get_by_role("button", name="Copy link" # ou "Copiar ligação" em PT
                     ).wait_for(state="visible")
    page.get_by_role("button", name="Copy link").click()

    link_input = page.locator('input[readonly][value^="http"]').first
    link_input.wait_for(state="visible")
    link_copiado = link_input.input_value()

    browser.close()

    print("Link copiado:", link_copiado)

    # Para funcionar como suposto, teremos de usar o link do comentário 
        # Iniciar sessão com a conta que contém o forms = FEITO
        # Clicar nas opções necessárias para criar um link pre-preenchido = FEITO
        # Preencher os campos de acordo com os campos do utilizador = +/- FEITO
        # Copiar o link e guardá-lo no excel = Copiar FEITO guardar NÃO FEITO
