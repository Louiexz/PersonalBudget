# PersonalBudget
Website - PersonalBudget: Take Control of Your Finances Quickly and Easily

## Funcionalidades e/ou (Páginas)

    Users: Permite que novos usuários criem uma conta.
    Goals: Permitir que os usuários estabeleçam, monitorem e gerenciem suas metas financeiras, como economizar para uma viagem.
    Budgets: Permitir que os usuários criem, gerenciem e monitorem orçamentos, ajudando-os a controlar suas finanças.
    Transactions categories: Facilitar a organização e análise das transações financeiras dos usuários, permitindo que eles categorizaram suas receitas.
    Transactions: Permitir que os usuários registrem, organizem e analisem suas transações financeiras.
    Dashboard: Fornecer uma visão consolidada e interativa das finanças do usuário, permitindo que ele monitore seus orçamentos, metas, categorias de transações e transações de forma rápida e eficiente.

## Pré-requisitos

### Certifique-se de ter o seguinte instalado antes de começar:
  
     Python 3

## Instalação e Uso

1. siga os seguintes passos:

- Clone o repositório:

        git clone https://github.com/Louiexz/PersonalBudget.git
        cd PersonalBudget
 
 - Para funcionar:

        Crie e ative um ambiente virtual (venv): https://docs.python.org/pt-br/3/library/venv.html

 - Instale as dependências:

        pip install -r requirements.txt
 
 - Realize as migrações

        python manage.py migrate

 - Execute o aplicativo:

        python manage.py runserver

 5. Acesse o chat:

    - Acesse o link ou abra um navegador e vá para http://127.0.0.1:8000/

## Estrutura do Projeto

myproject/
│
├── run.py
├── myproject/          # Diretório do projeto
│   ├── __init__.py
│   ├── settings.py     # Configurações do projeto
│   ├── urls.py         # Mapeamento de URLs
│   ├── asgi.py         # Configuração para ASGI
│   └── wsgi.py         # Configuração para WSGI
│
├── personalbudgets/   # Um aplicativo Django
│   ├── migrations/     # Arquivos de migração de banco de dados
│   ├── model/          # Diretório dos modelos de dados
│   ├── static/         # Diretório de arquivos estaticos (css, js, img)
│   ├── templates/      # Diretório dos templates html
│   ├── views/          # Diretório das lógicas de visualizações
│   ├── __init__.py
│   ├── admin.py        # Configurações do admin
│   ├── apps.py         # Configurações do aplicativo
│   ├── tests.py        # Testes do aplicativo
│   └── urls.py         # URLs específicas do aplicativo
│
├── manage.py           # Script de gerenciamento do projeto
│
├── requirements.txt    # Dependências do projeto
│
└── db.sqlite3          # Banco de dados SQLite (Criado com o migrate)

## Contribuições

Artur Ramos - 
Carlos Eduardo - carlos-1ima
Luiz Augusto - Louiexz
Paulo Arthur -
Vinicius José - ViniciusRKX

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
