from db.conexao import conecta_db

def listar_cliente(conexao):
    cursor = conexao.cursor()
    cursor.execute("select id, sexo, nome, telefone, senha, observacao from clientes by order id asc")
    registros = cursor.fetchall()
    return registros

def consultar_cliente_id(conexao):
    id = input("Digite o ID: ")
    cursor = conexao.cursor()
    cursor.execute("select id, sexo, nome, telefone, senha, observacao from clientes where id = " + id)
    registros = cursor.fetchall()
    return registros

def inserir_cliente(conexao, sexo, nome, telefone, senha, observacao):
    cursor = conexao.cursor()
    sql_insert = "insert into clientes (sexo, nome, telefone, senha, observacao) values ( %s, %s, %s, %s, %s)"
    dados = (sexo, nome, telefone, senha, observacao)
    cursor.execute(sql_insert, dados)
    conexao.commit()

def atualizar_cliente(conexao, id, sexo, nome, telefone, senha, observacao):
    cursor = conexao.cursor()
    sql_update = """update clientes set sexo = %s, nome = %s, telefone = %s, senha = %s, observacao = %s 
                    where id = %s"""
    dados = (sexo, nome, telefone, senha, observacao, id)   
    cursor.execute(sql_update, dados)
    conexao.commit()

def deletar_cliente(conexao, id):
    print("Deletando Cliente")
    cursor = conexao.cursor()
    sql_delete = "delete from clientes where id = "+ id
    cursor.execute(sql_delete)
    conexao.commit()
