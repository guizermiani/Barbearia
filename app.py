from flask import Flask, render_template, request, redirect, url_for, jsonify
from db.conexao import conecta_db
from db.barbearia_bd import consultar_barbearia_bd, inserir_barbearia_bd, alterar_barbearia_bd
from db.cliente_bd import listar_cliente, inserir_cliente
from db.profissionais_bd import listar_profissionais_bd, inserir_profissionais_bd
from db.servicos_bd import listar_servicos_bd, inserir_servicos_bd
from db.login_bd import login_profissional_bd, login_cliente_bd
from db.agendamento_bd import inserir_agendamento_bd, listar_agendamento_bd

app = Flask(__name__)

# login

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        # Valida campos obrigatórios; ajuste aqui para autenticar de verdade
        if not usuario or not senha:
            erro = "Preencha usuário e senha para entrar."
            return render_template("login.html", erro=erro)
        
        conexao = conecta_db()
        valida_login = login_profissional_bd(conexao,usuario, senha)
        # Antes de redirecionar vamos fazer a validação do usuario e senha

        if valida_login == "OK":
            return redirect(url_for('home'))
        else:
            return render_template("login.html",erro=valida_login)
        
    # Obriga a passar no login.html    
    return render_template("login.html")

@app.route('/login/cliente', methods=['GET','POST'])
def login_cliente():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        # Valida campos obrigatórios; ajuste aqui para autenticar de verdade
        if not usuario or not senha:
            erro = "Preencha usuário e senha para entrar."
            return render_template("login_cliente.html", erro=erro)
        
        conexao = conecta_db()
        valida_login = login_cliente_bd(conexao,usuario, senha)
        # Antes de redirecionar vamos fazer a validação do usuario e senha

        if valida_login == "OK":
            return redirect(url_for('area_cliente'))
        else:
            return render_template("login_cliente.html",erro=valida_login)
        
    # Obriga a passar no login.html    
    return render_template("login_cliente.html")



#barber
@app.route("/home")
def home():
    nome = "Sistema de Barbearia"
    return render_template("home.html" , nome=nome)

@app.route("/area_cliente")
def area_cliente():
    nome = "Área do Cliente"
    return render_template("area_cliente.html", nome=nome)

@app.route("/")
def index():
    return redirect(url_for("home"))

@app.route("/barbearias/novo", methods=['GET','POST'])
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

@app.route("/barbearias/listar", methods=['GET','POST'])
def barbearia_listar():
    conexao = conecta_db()
    barbearias = consultar_barbearia_bd(conexao)
    return render_template("barbearia_listar.html", barbearias=barbearias)

# agendamentos

@app.route("/agendamentos/listar", methods=['GET','POST'])
def agendamento_listar():
    conexao = conecta_db()
    agendamentos = listar_agendamento_bd(conexao)
    return render_template("agendamento_listar.html", agendamentos=agendamentos)

@app.route("/agendamentos/novo", methods=['GET','POST'])
def salvar_agendamento():
    conexao = conecta_db()
    barbeiros = listar_profissionais_bd(conexao)
    servicos = listar_servicos_bd(conexao)

    if request.method == "POST":
        id_cliente = request.form.get("id_cliente")
        id_profissional = request.form.get("id_profissional")
        id_servico = request.form.get("id_servico")
        data_hora = request.form.get("data_hora")
        valor_servico = request.form.get("valor_servico")
        status = request.form.get("status")

        
        inserir_agendamento_bd(conexao, id_cliente, id_profissional, id_servico, data_hora, valor_servico, status  )
        

        return f"<h2> Agendamento salvo com sucesso! </h2>"
   
    return render_template("agendamento_form.html", barbeiros = barbeiros, servicos = servicos)






#cliente

@app.route("/salvar/cliente", methods=["GET", "POST"])
def salvar_cliente():
    if request.method == "POST":
        nome = request.form.get("nome")
        sexo = request.form.get("sexo")
        telefone = request.form.get("telefone")
        senha = request.form.get("senha")
        observacao = request.form.get("observacao")

        if not nome:
            return "<h3> Por favor, preencha o nome</h3>"

        conexao = conecta_db()
        inserir_cliente(conexao, sexo, nome, telefone, senha, observacao)

        return f"<h2> Cliente salvo com sucesso: {nome} </h2>"

    return render_template("cliente_form.html", titulo="Cadastrar Cliente")

@app.route("/listar/clientes", methods=["GET"])
def listar_clientes():
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, sexo, nome, telefone, senha, observacao FROM clientes ORDER BY id DESC"
    )
    clientes = cursor.fetchall()
    return render_template("cliente_list.html", clientes=clientes, titulo="Clientes")

#profissionais

@app.route("/profissionais/listar", methods=["GET", "POST"])
def profissional_listar():
    conexao = conecta_db()
    profissionais = listar_profissionais_bd(conexao)
    return render_template("profissional_listar.html", profissionais=profissionais)

@app.route("/profissionais/novo", methods=["GET", "POST"])
def profissional_salvar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')
        
        if not nome or not senha:
            return "<h3> Por favor, preencha todos os campos</h3>"
        
        conexao = conecta_db()
        inserir_profissionais_bd(conexao,nome,telefone,senha)

        return f"<h2> Profissional Salvo com Sucesso:  {nome} </h2>"
    return render_template("profissional_form.html")

# servicos

@app.route("/servicos/listar", methods=["GET", "POST"])
def servico_listar():
    conexao = conecta_db()
    servicos = listar_servicos_bd(conexao)
    return render_template("servico_list.html", servicos=servicos)

@app.route("/servicos/novo", methods=["GET", "POST"])
def servico_salvar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        tempo_estimado = request.form.get('tempo_estimado')
        valor_servico = request.form.get('valor_servico')
        
        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3>"
        
        conexao = conecta_db()
        inserir_servicos_bd(conexao, nome, tempo_estimado, valor_servico)

        return f"<h2> Serviço Salvo com Sucesso:  {nome} </h2>"
    return render_template("servico_form.html")


if __name__ == "__main__":
    app.run(debug=True)
