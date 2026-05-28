from pytest_bdd import scenarios
import projetos.Fluxo.steps.steps

# Puxa os cenários do BDD
scenarios('./projetos/Fluxo/features')
# O gancho do teste fica 100% vazio, sem receber (page) e sem comandos dentro!
def test_fluxo():
    pass