from db.conexao import conecta_db
import bcrypt

def listar_cliente(conexao):
    cursor = conexao.cursor()
    cursor.execute("select id, sexo, nome, telefone, senha, observacao from clientes order by id asc")
    registros = cursor.fetchall()
    return registros

def consultar_cliente_id(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("select id,nome,sexo,telefone,senha,observacao from clientes where id = " + str(id))
    registro = cursor.fetchone()
    
    if registro is None:
        return None
    else:
        return registro

def inserir_cliente(conexao, sexo, nome, telefone, senha, observacao):
    senha = senha.encode("utf-8")
    salt = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha, salt)
    print("Hash senha:", hash_senha)


    cursor = conexao.cursor()
    sql_insert = "insert into clientes (sexo, nome, telefone, senha, observacao ) values ( %s, %s, %s, %s, %s)"
    dados = (sexo, nome, telefone, hash_senha.decode('utf-8'), observacao)

    cursor.execute(sql_insert, dados)
    conexao.commit()

def atualizar_cliente(conexao,sexo, nome, telefone, observacao, id):
    cursor = conexao.cursor()
    sql_update = """update clientes set sexo = %s, nome = %s, telefone = %s, observacao = %s 
                    where id = %s"""
    dados = (sexo, nome, telefone, observacao, id)   
    cursor.execute(sql_update, dados)
    conexao.commit()

def deletar_cliente(conexao, id):
    print("Deletando Cliente")
    cursor = conexao.cursor()
    sql_delete = "delete from clientes where id = "+ id
    cursor.execute(sql_delete)
    conexao.commit()
