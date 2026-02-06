from db.conexao import conecta_db
import bcrypt

def inserir_profissionais_bd(conexao, nome, telefone, senha):
    cursor = conexao.cursor()
    # criptografia de senha
    senha = senha.encode("utf-8")
    salt = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha, salt)
    print("Hash senha:", hash_senha)


    sql_insert = "insert into profissionais (nome, telefone, senha) values (%s, %s, %s)"
    dados = (nome, telefone, hash_senha.decode('utf-8'))
    cursor.execute(sql_insert, dados)
    conexao.commit()

def listar_profissionais_bd(conexao):
    cursor = conexao.cursor()
    sql_select = "select nome, telefone from profissionais"
    cursor.execute(sql_select)
    registros = cursor.fetchall()
    return registros