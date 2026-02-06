from db.conexao import conecta_db
import bcrypt

def login_profissional_bd(conexao, login, senha) -> str:
    cursor = conexao.cursor()
    cursor.execute("SELECT id, telefone, senha FROM profissionais WHERE telefone = %s", (login,))
    registro = cursor.fetchone()
    
    if registro: # Verificando se o usuario foi encontrado
        senha_verificar = senha.encode("utf-8")

        senha_bd = registro[2]

        if isinstance(senha_bd, str):
            senha_bd_bytes = senha_bd.encode("utf-8")
        else:
            senha_bd_bytes = senha_bd

        if bcrypt.checkpw(senha_verificar, senha_bd_bytes):
            return "OK"
        else: 
            return "Senha Inválida!"
    else:
        return "Usuário não encontrado!"
    

def login_cliente_bd(conexao, login, senha) -> str:
    cursor = conexao.cursor()
    cursor.execute("SELECT id, telefone, senha FROM clientes WHERE telefone = %s", (login,))
    registro = cursor.fetchone()
    
    if registro: # Verificando se o usuario foi encontrado
        senha_verificar = senha.encode("utf-8")

        senha_bd = registro[2]

        if isinstance(senha_bd, str):
            senha_bd_bytes = senha_bd.encode("utf-8")
        else:
            senha_bd_bytes = senha_bd

        if bcrypt.checkpw(senha_verificar, senha_bd_bytes):
            return "OK"
        else: 
            return "Senha Invalida  !"
    else:
        return "Usuário não encontrado !"