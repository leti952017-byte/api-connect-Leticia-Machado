from flask import jsonify, request
from data.usuarios_data import usuarios, gerar_novo_id


def listar_usuarios():
    return jsonify({
        "data": usuarios
    }), 200


def buscar_usuario_por_id(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuário não encontrado"
        }), 404

    return jsonify({
        "data": usuario
    }), 200


def cadastrar_usuario():
    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({
            "error": "O corpo da requisição deve conter dados em formato JSON."
        }), 400

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return jsonify({
            "error": "Os campos 'nome' e 'email' são obrigatórios."
        }), 400

    if not isinstance(nome, str) or not isinstance(email, str):
        return jsonify({
            "error": "Os campos 'nome' e 'email' devem ser do tipo String."
        }), 400

    nome = nome.strip()
    email = email.strip()

    if not nome or not email:
        return jsonify({
            "error": "Os campos 'nome' e 'email' não podem estar vazios."
        }), 400

    email_existente = any(
        usuario["email"].lower() == email.lower()
        for usuario in usuarios
    )

    if email_existente:
        return jsonify({
            "error": "Já existe um usuário cadastrado com este e-mail."
        }), 400

    novo_usuario = {
        "id": gerar_novo_id(),
        "nome": nome,
        "email": email
    }

    usuarios.append(novo_usuario)

    return jsonify({
        "data": novo_usuario
    }), 201


def atualizar_usuario(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuário não encontrado"
        }), 404

    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({
            "error": "O corpo da requisição deve conter dados em formato JSON."
        }), 400

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return jsonify({
            "error": "Os campos 'nome' e 'email' são obrigatórios."
        }), 400

    if not isinstance(nome, str) or not isinstance(email, str):
        return jsonify({
            "error": "Os campos 'nome' e 'email' devem ser do tipo String."
        }), 400

    usuario["nome"] = nome.strip()
    usuario["email"] = email.strip()

    return jsonify({
        "data": usuario
    }), 200


def remover_usuario(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuário não encontrado"
        }), 404

    usuarios.remove(usuario)

    return jsonify({
        "data": {
            "mensagem": "Usuário removido com sucesso"
        }
    }), 200
