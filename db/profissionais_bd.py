from db.conexao import conecta_db

def inserir_profissionais_bd(conexao, nome, telefone, senha):
    cursor = conexao.cursor()
    sql_insert = "insert into profissionais (nome, telefone, senha) values (%s, %s, %s)"
    dados = (nome, telefone, senha)
    cursor.execute(sql_insert, dados)
    conexao.commit()

def listar_profissionais_bd(conexao):
    cursor = conexao.cursor()
    sql_select = "select nome, telefone from profissionais"
    cursor.execute(sql_select)
    registros = cursor.fetchall()
    return registros