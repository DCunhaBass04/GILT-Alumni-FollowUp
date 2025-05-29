# Criar respostas pre-preenchidas para utilizadores recorrentes

Precisaremos de criar um *script* que, dado os dados referentes a utilizadores que já responderam uma vez (ou mais) ao inquérito, crie e guarde links pre-preenchidos para enviar a esses mesmos utilizadores no ano seguinte.

**Nota:** Isto é necessário fazer com um script exterior visto que o **Microsoft Forms** não fornece uma API que permita criar um link pre-preenchido automaticamente.

Isto será feito pelo script [**create_prefilled_forms.py**](../../src/create_prefilled_form.py). Este script irá, para cada utilizador recorrente, utilizar **Playwright** para simular os cliques necessários para criar um link pre-preenchido e guardá-lo no mesmo ficheiro *excel* que contém a resposta.

Esta funcionalidade exige o *setup* seguinte:

## Configuração do *pandas*

Na *virtual environment*, execute os seguintes comandos:

```sh
pip install pandas
pip install openpyxl
```