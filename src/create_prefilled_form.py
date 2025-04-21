from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, slow_mo=100) # headless=True quando usar na VM
                                                            # headless=False para demonstrar
    page = browser.new_page()
    page.goto("https://forms.office.com/e/UjMY4ZD44w?origin=lprLink")
    # Link a usar será https://forms.office.com/Pages/DesignPageV2.aspx?prevorigin=shell&origin=NeoPortalPage&subpage=design&id=KaZgeh_mDEOcYyZmU7K4mdJHUj9O90RKqZcCemQF4EZUQktKVE9HTlhMWjRUREtERkdWV1UySkpWTS4u

    # Esperar até os inputs serem visíveis
    page.locator('input').nth(0).wait_for()

    # Preencher campos de texto
    page.fill('input >> nth=0', "diogo10072004@isep.ipp.pt")    # 1º campo
    page.fill('input >> nth=1', "Diogo Teste Playwright")       # 2º campo

    # Clicar na primeira opção que contém "Sim"
    page.get_by_text("Sim", exact=True).nth(0).click()

    # Screenshot do resultado preenchido (opcional)
    page.screenshot(path="demonstracao.png")

    browser.close()

    # Por agora, só estamos a preencher um par de campos e tirar uma print.
    # Para funcionar como suposto, teremos de usar o link do comentário 
        # Iniciar sessão com a conta que contém o forms
        # Clicar nas opções necessárias para criar um link pre-preenchido
        # Preencher os campos de acordo com os campos
        # Copiar o link e guardá-lo
