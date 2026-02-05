from db.conexao import conecta_db

def inserir_servicos_bd(conexao, nome, tempo_estimado, valor_servico):
    cursor = conexao.cursor()
    sql_insert = "insert into servico (nome, tempo_estimado, valor_servico) values (%s, %s, %s)"
    dados = (nome, tempo_estimado, valor_servico)
    cursor.execute(sql_insert, dados)
    conexao.commit()

def listar_servicos_bd(conexao):
    cursor = conexao.cursor()
    sql_select = "select nome, tempo_estimado, valor_servico from servico"
    cursor.execute(sql_select)
    registros = cursor.fetchall()
    return registros