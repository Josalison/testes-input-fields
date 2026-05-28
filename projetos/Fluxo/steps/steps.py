from pytest_bdd import given, when, then
import pytest
from projetos.Fluxo.page.ir_site import AcessarSite

@pytest.fixture
def site(page) -> AcessarSite:
    return AcessarSite(page)

@given('que estou na página de input fields')
def acessar_pagina(site: AcessarSite):
    site.acessar_site()

@when('preencho o nome do filme e texto adicional')
def digitar_nome_filme(site: AcessarSite):
    site.Digitar_nome_do_filme()

@when('apago o texto do campo')
def apagar(site:AcessarSite):
    site.apagar_texto_do_campo()

@then('verifico o texto do campo')
def VerificarTexto(site:AcessarSite):
    site.verificar_texto()

@then('verifico que o campo está desabilitado')
def v_campo(site:AcessarSite):
    site.verificar_campo_desabilitado()

@then('verifico que o campo é somente leitura')
def v_campo_de_leitura(site:AcessarSite, page):
    site.verificar_campo_de_leitura()
    page.wait_for_timeout(10000)
