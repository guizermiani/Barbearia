from db.conexao import conecta_db

def consultar_barbearia_bd(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
                select id, nome, telefone, endereco, forma_pagamento
                from barbearia order by id asc""")
    registros = cursor.fetchall()
    return registros


def inserir_barbearia_bd(conexao, nome, telefone, endereco, forma_pagamento):
    cursor = conexao.cursor()
    sql_insert = """insert into barbearia (nome, telefone, endereco, forma_pagamento)
                    values (%s, %s, %s, %s)"""
    dados = (nome, telefone, endereco, forma_pagamento)
    cursor.execute(sql_insert, dados)
    conexao.commit()

def alterar_barbearia_bd(conexao, id, nome, telefone, endereco, forma_pagamento):
    cursor = conexao.cursor()
    sql_update = """update barbearia set nome = %s, telefone = %s, endereco = %s, forma_pagamento = %s 
                    where id = %s"""
    # ID eh o ultimo campo a ser passado para o array de dados
    dados = (nome, telefone, endereco, forma_pagamento, id)
    cursor.execute(sql_update, dados)
    conexao.commit()