from db.conexao import conecta_db

def inserir_agendamento_bd(conexao, id_cliente, id_profissional, id_servico, data_hora, valor_servico, status):
    cursor = conexao.cursor()

    sql_insert = """insert into agendamento (id_cliente, id_profissional, id_servico, data_hora,
                    valor_servico, status)
                    values (%s, %s, %s, %s, %s, %s)"""
    dados = (id_cliente, id_profissional, id_servico, data_hora, valor_servico, status)
    cursor.execute(sql_insert, dados)
    conexao.commit()


def listar_agendamento_bd(conexao):
    cursor = conexao.cursor()
    sql_select = """select
                    id_cliente, id_profissional, id_servico, data_hora, valor_servico,
                    status from agendamento """
    cursor.execute(sql_select)
    registros = cursor.fetchall()
    return registros