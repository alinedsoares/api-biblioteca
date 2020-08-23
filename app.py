from flask import Flask, jsonify, request
import json

app = Flask(__name__)

livros = [
    {'id_livro': 0, 'nome_livro': 'Milagre da Manhã', 'status_livro': 'EMPRESTADO'},
    {'id_livro': 1, 'nome_livro': 'O Poder do Hábito', 'status_livro': 'DISPONÍVEL'},
    {'id_livro': 2, 'nome_livro': 'A Sutil Arte de Ligar o Foda-se', 'status_livro': 'DISPONÍVEL'},
    {'id_livro': 3, 'nome_livro': 'A Arte da Guerra', 'status_livro': 'EMPRESTADO'},
    {'id_livro': 4, 'nome_livro': 'Manual de Python', 'status_livro': 'DISPONÍVEL'}
]
# O campo emprestimo exibe o id_livro dos livros emprestados ao cliente
clientes = [
    {'id_cliente': 0, 'nome_cliente': 'Madrugador Feliz', 'emprestimos': ['0', '3']},
    {'id_cliente': 1, 'nome_cliente': 'Metódico Seletivo', 'emprestimos': []},
    {'id_cliente': 2, 'nome_cliente': 'Tô nem aí', 'emprestimos': []},
    {'id_cliente': 3, 'nome_cliente': 'Estrategista Seguro ', 'emprestimos': []},
    {'id_cliente': 4, 'nome_cliente': 'Aline Soares', 'emprestimos': []}
]  # TODO: INSERIR VÍNCULO COM BANCO DE DADOS E VERIFICAR COMO INSERIR OS SCRIPTS


# Consulta de todos os livros emprestados para o cliente usando GET #TODO: UTILIZAR ENCARGOS.PY PARA RETORNAR O CÁLCULO DE VALOR A PAGAR
@app.route('/client/<int:id>/books/', methods=['GET'])
def visualizar_cliente(id):
    try:
        visualiza_cliente = clientes[id]
    except IndexError:
        visualiza_cliente = {'id_cliente': 'cliente não cadastrado.'}
    return jsonify(visualiza_cliente)


# Consulta de livro por id usando GET
@app.route('/books/<int:id>/', methods=['GET'])
def livro(id):
    try:
        livro = livros[id]
    except IndexError:
        livro = {'id_livro': 'id_livro não foi localizado no acervo.'}
    return jsonify(livro)


# Reserva de livros usando PUT #TODO: PERMITIR ALTERAÇÃO APENAS DO CAMPO 'status_livro'
@app.route('/books/<int:id>/reserve', methods=['PUT'])
def reservar_livro(id):
    atualizacao = json.loads(request.data)
    livros[id] = atualizacao
    return jsonify(atualizacao)


# Consulta de todos os livros do acervo usando GET
@app.route('/books/', methods=['GET'])
def visualizar_livros():
    livro = livros
    return jsonify(livro)


if __name__ == '__main__':
    app.run(debug=True)
