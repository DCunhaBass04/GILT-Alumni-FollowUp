# Manipulação do *Forms*

As funcionalidades aqui colocadas exigem uma manipulação/simulação automática da página do *Microsoft Forms*, visto que esta não fornece uma API para o que se pretende:
* [Criar URLs pré-preenchidos](create_prefilled_forms/readme.md)
* [Ativar/Desativar *Forms*](page_toggle/readme.md)

Isto será feito através da lib ***Playwright*** do python. 

Estas funcionalidades exigem o *setup* seguinte:

## Instalação do python

```sh
apt install python3
```

## Instalação da lib Playwright

```sh
pip install playwright
playwright install
```

## Configuração do ficheiro credentials.cfg

Na base do repositório (no mesmo nível que o ficheiro **conf.cfg**) encontra-se um ficheiro **credentials.cfg** colocado no **.gitignore** para segurança. Este é o formato do ficheiro:

```ini
[CREDENTIALS]
email=...
password=...
```

Estas credenciais são utilizadas para iniciar sessão como *admin* da página **Microsoft Forms**.