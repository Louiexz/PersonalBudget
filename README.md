# PersonalBudget
Website - PersonalBudget: Take Control of Your Finances Quickly and Easily

## Funcionalidades

    Chat em Tempo Real: Mensagens são enviadas e recebidas instantaneamente sem a necessidade de atualizar a página.
    Múltiplos Usuários: Vários usuários podem se conectar ao chat ao mesmo tempo.
    Sala de Chat: Os usuários podem enviar mensagens para todos na sala.
    Histórico de Mensagens: O chat mantém um histórico das mensagens recentes.
    Interface Simples: Interface web simples e intuitiva.

## Pré-requisitos

### Certifique-se de ter o seguinte instalado antes de começar:
  
     Python 3
     Flask
     Flask-SocketIO

## Instalação e Uso

1. siga os seguintes passos:

- Clone o repositório:

        git clone https://github.com/Louiexz/PersonalBudget.git
        cd PersonalBudget
 
 - Para funcionar:

        Crie e ativa um ambiente virtual (venv): https://docs.python.org/pt-br/3/library/venv.html

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
Louiexz - Autor e Desenvolvedor do site<br>

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
