from flask import Flask, jsonify
from routes.usuarios_routes import usuarios_bp


def create_app(config=None):
    app = Flask(__name__)

    # Mantém a depuração desligada no servidor publicado.
    app.config["DEBUG"] = False

    # Permite passar configurações extras nos testes, se necessário.
    if config:
        app.config.update(config)

    # Registra as rotas de usuários.
    app.register_blueprint(usuarios_bp)

    # Página inicial da API.
    @app.route("/", methods=["GET"])
    def inicio():
        return jsonify({
            "data": {
                "mensagem": "API Connect funcionando com sucesso!"
            }
        }), 200

    # Verifica se a aplicação está respondendo.
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify(status="ok"), 200

    return app


# Permite executar localmente. No Render, o Gunicorn inicia a aplicação.
if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=False)
