# Delivery System Express API

# Guia de Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/OPE-Virtual-Solutions/dse-api.git
    ```
2. Abra o diretório do projeto e crie uma máquina virtual Python
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

3. Crie um arquivo chamado `.env` no diretório raíz do projeto e coloque dentro dele a seguinte configuração:
    ```
    DATABASE_NAME=NOME_DO_BANCO_DE_DADOS
    DATABASE_USER=NOME_DO_USUARIO_PARA_LOGIN
    DATABASE_PASSWORD=NOME_DE_SENHA_PARA_LOGIN
    DATABASE_HOST=localhost
    DATABASE_PORT=1433
    ```

    **OBS.:** Os valores após o `=` deverão ser trocados de acordo com a configuração do seu banco de dados, sendo:
    - `DATABASE_NAME` - Nome do banco de dados que será utilizado na API;
    - `DATABASE_USER` - Nome do usuário para logon no SQL Management Studio;
    - `DATABASE_PASSWORD` - Senha do usuário.

4. Instale as dependências necessárias para a execução do projeto:
    ```bash
    # aponte o terminal para dentro da primeira pasta "LeandroLanches" e execute
    pip install -r requirements.txt
    ```

5. Sincronize o `django` com o banco de dados conectado:
    ```bash
    # cria as migrations do próprio django 
    python manage.py makemigrations

    # adiciona as migrations ao banco de dados
    python manage.py migrate
    ```

6. Rode a aplicação:
    ```bash
    python manage.py runserver
    ```
