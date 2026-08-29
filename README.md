# API Connect

API REST desenvolvida para gerenciamento de usuários, criada como um Produto Mínimo Viável (MVP).

O projeto permite realizar operações de cadastro, consulta, atualização e remoção de usuários através do protocolo HTTP, utilizando respostas padronizadas em formato JSON.

## Tecnologias utilizadas

- Python
- Flask
- HTTP
- JSON
- Git
- GitHub
- Thunder Client para testes da API

## Estrutura do projeto

```text
api_connect/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── routes/
│   ├── __init__.py
│   └── usuarios_routes.py
│
├── controllers/
│   ├── __init__.py
│   └── usuarios_controller.py
│
└── data/
    ├── __init__.py
    └── usuarios_data.py
    ## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/api-connect-seu-nome-sobrenome.git
