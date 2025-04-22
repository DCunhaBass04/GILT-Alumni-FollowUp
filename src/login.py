def login(page, email, password):

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