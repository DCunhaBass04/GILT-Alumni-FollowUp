# Extrair *excel* com endereços autorizados e respostas

Precisaremos de criar um *script* que, dado as credenciais da conta que contém o *sharepoint* onde está o ficheiro com os endereços autorizados, extrai-o para o sistema local (de forma a ser utilizado por outras funcionalidades).

Isto será feito pelo script [**mount_sharepoint.sh**](../../src/mount_sharepoint.sh). Este script irá criar um clone de todos os ficheiros no caminho fornecido do *sharepoint*, permitindo que a máquina virtual veja o ficheiro e altere-o se necessário.

Esta funcionalidade exige o *setup* seguinte:

## Configuração do *rclone*

```sh
sudo apt install rclone
rclone config
```

Após esta seguinte linha, as configurações são as seguintes:
1. Pressionar **n** para criar um novo *remote*.
2. Dar o nome "sharepoint" ao novo *remote*.
3. Escolher a opção 30 "Microsoft OneDrive".
4. Não entrar na configuração avançada nem na automática.
5. Num computador local, faça o seguinte:
    1. Executar a seguinte linha:

        ```sh
        rclone authorize "onedrive"
        ```
    2. Inicie sessão na conta **Microsoft** que tem acesso ao **sharepoint**. Deverá obter um bloco com o seguinte formato:
        ```json
        {"access_token":"...", "token_type":"Bearer", ...}
        ```
6. Copie este bloco todo e cole-o quando aparecer "**config_token>**" o processo na máquina virtual.
7. Escolha a opção 4 "Search for a Sharepoint site".
8. Pesquise o nome do site Sharepoint que contém o ficheiro *excel*.

## Configuração do script

Instale a dependência "fuse3":

```sh
apt install fuse3
```

Verifique que este ficou corretamente instalado executando esta linha:

```sh
cat /proc/filesystems | grep fuse
```

Este estará corretamente instalado se aparecer algo como:

```nginx
nodev   fuse
```

Agora, para que a montagem local do Sharepoint seja feita sempre que a máquina virtual for ligada, precisa de fazer o seguinte:

1. Editar o ficheiro **/etc/systemd/system/sharepoint-mount.service**:
    ```ini
    [Unit]
    Description=Montar SharePoint via Rclone no arranque
    After=network-online.target
    Wants=network-online.target

    [Service]
    Type=simple
    ExecStart=/bin/bash /root/mount_sharepoint.sh
    Restart=always
    TimeoutSec=30

    [Install]
    WantedBy=multi-user.target
    ```
2. De seguida, execute as seguintes linhas para colocar o sistema a funcionar:
    ```sh
    systemctl daemon-reload
    systemctl restart sharepoint-mount
    ```
3. Para verificar que o serviço está a rodar corretamente, rode o seguinte:
    ```
    systemctl status sharepoint-mount
    ```
    Se correu bem, deverá aparecer algo como:
    ```arduino
    Active: active (running)
    ```