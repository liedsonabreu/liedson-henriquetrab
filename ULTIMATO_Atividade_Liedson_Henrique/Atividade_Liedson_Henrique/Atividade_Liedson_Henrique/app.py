from config.Config import Config
from config.Database import Database
from dao.ProdutoDao import ProdutoDao
from model.Produto import Produto
from flask import Flask, request, render_template

app = Flask(__name__)

dao = ProdutoDao(Database(Config().config).conn)

@app.route('/', methods=["GET"]) 
def main(): 
    return render_template("main.html")

@app.route('/produto/novo', methods=["GET"]) 
def novo(): 
    return render_template("inserir.html")

@app.route('/produto/', methods=["POST"]) 
def inserir(): 
    produto = Produto()

    produto.nome = request.form.get("nome")
    produto.preco = request.form.get("preco")
    produto.quantidade = request.form.get("quantidade")
  
    dao.inserirProduto(produto)

    lista = dao.selecionarProdutos()
    return render_template(
        "listagem.html",
        lista=lista
        )

@app.route('/produto', methods=["GET"])
def listar():
    lista = dao.selecionarProdutos()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/produto/<id>', methods=["GET"])
def editarPagina(id):
    produto = dao.selecionarProduto(id)
    return render_template("editar.html", produto=produto)


@app.route('/produto/editar/', methods=["POST"])
def editar():
    produto = Produto()
    produto.id = request.form.get("id")
    produto.nome = request.form.get("nome")
    produto.preco = request.form.get("preco")
    produto.quantidade = request.form.get("quantidade")
    produto = dao.alterarProduto(produto)

    lista = dao.selecionarProdutos()
    return render_template(
        "listagem.html",
        lista=lista
    )


@app.route('/produto/remover/<id>', methods=["GET"])
def remover(id):
    produto = Produto()
    produto.id = id
    dao.excluirProduto(produto)

    lista = dao.selecionarProdutos()
    return render_template(
        "listagem.html",
        lista=lista
    )

if __name__=='__main__':
    app.run()



