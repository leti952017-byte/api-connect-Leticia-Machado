from flask import Flask, jsonify, render_template
from routes.usuarios_routes import usuarios_bp


def create_app(config=None):
    app = Flask(__name__)

    app.config["DEBUG"] = False

    if config:
        app.config.update(config)

    # Registra as rotas de usuários da API
    app.register_blueprint(usuarios_bp)

    # Mostra a página inicial
    @app.route("/", methods=["GET"])
   def inicio():
       return render_template("index.html")

    # Verifica se o servidor está funcionando
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify(status="ok"), 200

    return app


# Este trecho é usado quando você executa o projeto no seu computador.
# No Render, o Gunicorn inicia a aplicação.
if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=False)
