from db.barbearia_bd import consultar_barbearia_bd, inserir_barbearia_bd, alterar_barbearia_bd
from flask import Flask, Blueprint, render_template, request, redirect, session, url_for, jsonify
from db import conexao, conecta_db
from auth import login_required, login_required_cliente

barbearias = Blueprint('barbearias', __name__, url_prefix='/barbearias')

@barbearias.route("/barbearias/novo", methods=['GET','POST'])
@login_required
def salvar_barbearia():
    if request.method == 'POST':
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        formas_pagamento = request.form.get('formas_pagamento')

        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3"
        
        conexao = conecta_db()
        inserir_barbearia_bd(conexao,nome,telefone,endereco,formas_pagamento)

        return f"<h2> Barbearia Salva com Sucesso:  {nome} </h2>"
    return render_template("barbearia_form.html")

@barbearias.route("/barbearias/listar", methods=['GET','POST'])
@login_required
def barbearia_listar():
    conexao = conecta_db()
    barbearias = consultar_barbearia_bd(conexao)
    return render_template("barbearia_listar.html", barbearias=barbearias)