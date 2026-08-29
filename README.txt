API Connect - Projeto Flask

1) Abra a pasta api_connect no VS Code.
2) Abra Terminal > Novo Terminal.
3) Crie o ambiente virtual:
   py -m venv venv
4) Ative:
   .\venv\Scripts\activate
5) Instale as dependências:
   pip install -r requirements.txt
6) Execute:
   py app.py
7) Abra no navegador:
   http://127.0.0.1:5000

Testes principais no Postman:
- POST http://127.0.0.1:5000/usuarios
  Body JSON:
  {
    "nome": "Carlos Lima",
    "email": "carlos@email.com"
  }
  Esperado: 201

- POST http://127.0.0.1:5000/usuarios
  Body JSON:
  {
    "nome": "Pedro Santos"
  }
  Esperado: 400

- GET http://127.0.0.1:5000/usuarios
  Esperado: 200

- GET http://127.0.0.1:5000/usuarios/9999
  Esperado: 404
