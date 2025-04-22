# Manipulação do *Forms*

As funcionalidades aqui colocadas exigem uma manipulação/simulação automática da página do *Microsoft Forms*, visto que esta não fornece uma API para o que se pretende:
* [Criar URLs pré-preenchidos](create_prefilled_forms/readme.md)
* [Ativar/Desativar *Forms*](page_toggle/readme.md)

Isto será feito através da lib ***Playwright*** do python. 

Estas funcionalidades exigem o *setup* seguinte:

## Configuração de um *proxy*

Para a *Virtual Machine* poder aceder a websites como o *Forms*, teremos de configurar um *proxy* da seguinte forma **(assumindo que, na VM, usamos um utilizador "root" com password "hello" com o servidor "isep.ipp.pt" na porta 8080)**:

```sh
export http_proxy="http://root:hello@proxy.isep.ipp.pt:8080"
export https_proxy="http://root:hello@proxy.isep.ipp.pt:8080"
```

Poderá testar se este *proxy* funcionou a executar a seguinte linha:

```sh
curl -I https://forms.office.com
```

E deve receber uma resposta começada com **HTTP/1.0 200 Connection established**.

## Instalação do python

```sh
apt install python3
apt install python3-pip
```

## Configuração de *virtual environment*

Faça estes passos na base do repositório:

```sh
python3 -m venv venv
source venv/bin/activate
```

Isto vai fazer a máquina entrar no modo ***venv***

## Instalação da lib Playwright (no modo *venv*)

```sh
pip install playwright
playwright install
playwright install-deps
```

## Configuração do ficheiro credentials.cfg

Na base do repositório (no mesmo nível que o ficheiro **conf.cfg**) encontra-se um ficheiro **credentials.cfg** colocado no **.gitignore** para segurança. Este é o formato do ficheiro:

```ini
[CREDENTIALS]
email=...
password=...
```

Estas credenciais são utilizadas para iniciar sessão como *admin* da página **Microsoft Forms**.