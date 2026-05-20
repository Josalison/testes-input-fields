from playwright.sync_api import sync_playwright, expect
from page.pages import BasePages
class AcessarSite(BasePages):
    def acessar_site(self):
        self.page.goto("https://www.qaplayground.com/practice/input-fields")
        

    def Digitar_nome_do_filme(self):
        self.page.get_by_test_id("input-movie-name").fill("Lords of Rings")
        self.page.keyboard.press("Tab")
        self.page.get_by_test_id("input-append-text").fill("Meu precioso !!!")
        self.page.keyboard.press("Tab")
        
    def vericar_texto(self):
        expect(self.page.get_by_test_id("input-verify-text")).to_have_value("QA PlayGround")

    def apagar_texto_do_campo(self):
        self.page.get_by_test_id("input-clear-text").fill("")

    def verificar_campo_desabilitado(self):
        expect(self.page.get_by_test_id("input-disabled")).to_be_disabled()

    def verificar_campo_de_leitura(self):
        self.page.get_by_test_id("input-readonly").scroll_into_view_if_needed()
        expect(self.page.get_by_test_id("input-readonly")).to_have_attribute("readonly","")
        