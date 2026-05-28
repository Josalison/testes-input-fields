Feature: Testar campos de input no QA Playground

  Scenario: Preencher e validar campos da página
    given que estou na página de input fields
    when preencho o nome do filme e texto adicional
    then apago o texto do campo
    then verifico o texto do campo
    then verifico que o campo está desabilitado
    then verifico que o campo é somente leitura