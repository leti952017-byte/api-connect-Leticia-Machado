from flask import Flask, jsonify
from routes.usuarios_routes import usuarios_bp

app = Flask(__name__)

# Registra as rotas da API
app.register_blueprint(usuarios_bp)


@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "data": {
            "mensagem": "API Connect funcionando com sucesso!"
        }
    }), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
