# PersonalBudget
Website - PersonalBudget: Take Control of Your Finances Quickly and Easily

## Funcionalidades e/ou (Páginas)

    Users: Allow new users to create an account.
    Virtual Intelligence Assistant: Chat with the AI, get tips and have your questions answered (with limited usage on the free plan).
    Goals: Allow users to set, monitor, and manage their financial goals, such as saving for a trip.
    Budgets: Allow users to create, manage, and monitor budgets, helping them control their finances.
    Transaction Categories: Make it easy to organize and analyze users' financial transactions by allowing them to categorize their income. Transactions: Allow users to record, organize, and analyze their financial transactions.
    Dashboard: Provide a consolidated, interactive overview of the user's finances, enabling them to quickly and efficiently monitor their budgets, goals, transaction categories, and transactions.

## Pré-requisitos

### Certifique-se de ter o seguinte instalado antes de começar:
  
     Python 3
     Conta no Ollama (https://ollama.com/)

## Instalação e Uso (Teste)

- Acesse:
        https://personalbudget-ii4q.onrender.com/

## Instalação e Uso (Localmente)

1. Clone o repositório:

        git clone https://github.com/Louiexz/PersonalBudget.git
        cd PersonalBudget

2. Configure as variáveis de ambiente (crie um arquivo .env na raiz do projeto):

    DEBUG=False (Em caso de produção)
    SECRET_KEY= ("Gere uma com: python -c \"from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())\")
    ALLOWED_HOSTS=localhost,127.0.0.1
    API_TOKEN= (Criar key do Ollama: https://ollama.com/settings/keys)
     
3. Ambiente virtual (evita conflito com as dependências que possui):

        Crie e ative um ambiente virtual (venv): https://docs.python.org/pt-br/3/library/venv.html

4. Ative o ambiente virtual:

    - Linux (Git Bash):
        source .NomeDaPasta/bin/activate

    - Windows (Git Bash):
        "source venv/Scripts/activate" ou ". venv/Scripts/activate"

5. Instale as dependências:

        pip install -r requirements.txt
 
6. Realize as migrações

        python manage.py migrate

7. Execute o aplicativo:

        python manage.py runserver

8. Acesse o chat:

    - Acesse o link ou abra um navegador e vá para http://127.0.0.1:8000/

## Estrutura do Projeto

    PersonalBudget/
    │
    ├── run.py
    ├── api/             # Diretório do projeto
    │   ├── __init__.py
    │   ├── settings.py      # Configurações do projeto
    │   ├── urls.py          # Mapeamento de URLs
    │   ├── asgi.py          # Configuração para ASGI
    │   └── wsgi.py          # Configuração para WSGI
    │   
    ├── data/            # Dados para utilizar como exemplo
    │   ├── budgets.csv      # Orçamentos (CSV)
    │   ├── goals.json       # Metas (JSON)
    │   ├── categories.json  # Categorias de transações (JSON)
    │   └── transactions.csv # Histórico de transações (CSV)
    │   
    ├── docs/            # Documentações do projeto
    │   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
    │   ├── 02-base-conhecimento.md       # Estratégia de dados
    │   ├── 03-prompts.md                 # Engenharia de prompts
    │   ├── 04-metricas.md                # Avaliação e métricas
    │   └── 05-pitch.md                   # Roteiro do pitch
    │
    ├── personalbudgets/ # Aplicativo principal django
    │   ├── __init__.py
    │   ├── migrations/      # Arquivos de migração de banco de dados
    │   ├── model/           # Diretório dos modelos de dados
    │   ├── static/          # Diretório de arquivos estaticos (css, js, img)
    │   ├── templates/       # Diretório dos templates html
    │   ├── views/           # Diretório das lógicas de visualizações    
    │   ├── admin.py         # Configurações do admin
    │   ├── apps.py          # Configurações do aplicativo
    │   ├── tests.py         # Testes do aplicativo
    │   └── urls.py          # URLs específicas do aplicativo
    │
    ├── manage.py            # Script de gerenciamento do projeto
    │
    ├── requirements.txt     # Dependências do projeto
    │
    └── db.sqlite3           # Banco de dados SQLite (Criado com o migrate)

## Contribuições

Luiz Augusto - [@Louiexz](https://github.com/Louiexz)<br>

Contribuições restritas! Analisaremos issues e pull requests.