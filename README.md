# Delivery System Express API

# Guia de Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/OPE-Virtual-Solutions/dse-api.git
    ```
2. (opcional) Abra o diretório do projeto e crie uma máquina virtual Python
    ```bash
    # no Windows
    python -m venv venv

    # no Linux
    python3 -m venv venv
    ```

    2.1. Ative a máquina virtual através de um dos comandos (a depender do seu terminal):
    | Plataforma | Shell           | Comando para ativar o ambiente virtual |
    |------------|-----------------|----------------------------------------|
    | POSIX      | bash/zsh        | $ source venv/bin/activate           |
    |            | fish            | $ source venv/bin/activate.fish      |
    |            | csh/tcsh        | $ source venv/bin/activate.csh       |
    |            | PowerShell Core | $ venv/bin/Activate.ps1              |
    | Windows    | cmd.exe         | C:\> venv\Scripts\activate.bat       |
    |            | PowerShell      | PS C:\> venv\Scripts\Activate.ps1    |

3. Crie um arquivo chamado `.env` e coloque dentro dele a seguinte configuração:
    ```
    DATABASE_NAME=NOME_DO_BANCO_DE_DADOS
    DATABASE_USER=NOME_DO_USUARIO_PARA_LOGIN
    DATABASE_PASSWORD=NOME_DE_SENHA_PARA_LOGIN
    DATABASE_HOST=localhost
    DATABASE_PORT=1433
    ```

    Guia de parâmetros:
    - `DATABASE_NAME` - Nome do banco de dados que será utilizado na API;
    - `DATABASE_USER` - Nome do usuário para logon no SQL Management Studio;
    - `DATABASE_PASSWORD` - Senha do usuário.

4. Rode a aplicação:
```bash
# com máquina virtual 
python manage.py runserver
```