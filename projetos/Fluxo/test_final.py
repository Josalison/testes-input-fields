from playwright.sync_api import sync_playwright, expect
from page.ir_site import AcessarSite

def test_fluxo(page):
    acessar_site = AcessarSite(page)


    acessar_site.acessar_site()
    acessar_site.Digitar_nome_do_filme()
    acessar_site.vericar_texto()
    acessar_site.apagar_texto_do_campo()
    acessar_site.verificar_campo_desabilitado()
    acessar_site.verificar_campo_de_leitura()
    
    page.wait_for_timeout(3000)