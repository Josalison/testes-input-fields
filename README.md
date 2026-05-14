# 🎭 Automação de Testes — QA Playground (Input Fields)

Projeto de automação de testes utilizando **Playwright + Python** com o padrão **Page Object Model (POM)**, cobrindo os cenários de teste da página de campos de entrada do [QA Playground](https://www.qaplayground.com/practice/input-fields).

---

## 🛠️ Tecnologias utilizadas

- Python
- Playwright
- Pytest
- Page Object Model (POM)

---

## 📁 Estrutura do projeto

```
projetos/
└── Fluxo/
    ├── page/
    │   └── pages/
    │       ├── base_pages.py
    │       └── ir_site.py
    └── test_final.py
```

---

## ✅ Cenários de teste

### Cenário 1 — Inserção do nome do filme
Preenche o campo de nome do filme com o texto `"Lords of Rings"` utilizando o seletor `data-testid`.

### Cenário 2 — Adicionar texto e pressionar Tab
Preenche o campo de texto com `"Meu precioso !!!"` e pressiona a tecla **Tab**, verificando o comportamento de append do campo.

### Cenário 3 — Verificar texto presente no campo
Valida que o campo contém o texto `"QA PlayGround"` utilizando o `expect` do Playwright.

### Cenário 4 — Limpar o texto
Utiliza o método `clear()` para apagar o conteúdo de um campo de entrada e verifica que foi limpo corretamente.

### Cenário 5 — Verificar campo desabilitado
Valida que o campo de edição está desabilitado utilizando `to_be_disabled()`.

### Cenário 6 — Verificar campo somente leitura
Valida que o campo possui o atributo `readonly`, impedindo edição pelo usuário, utilizando `to_have_attribute("readonly", "")`.

---

## ▶️ Como executar

**1. Instale as dependências:**
```bash
pip install pytest playwright
playwright install
```

**2. Execute os testes:**
```bash
pytest projetos/Fluxo/test_final.py
```

---

## 📌 Observações

- Os elementos foram identificados manualmente via **DevTools (F12)** utilizando o atributo `data-testid`
- O projeto segue o padrão **POM** para melhor organização e reusabilidade do código
