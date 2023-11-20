import mysql.connector
from mysql.connector import Error


#conexao
connection = mysql.connector.connect(
    host='localhost',
    database='prog_gastos',
    user='root',
    password=''
)

cursor = connection.cursor()


#verificação de login
def verificar_login(name_user, pass_user):
    cursor.execute(f"SELECT pass_user FROM USUARIOS WHERE name_user = '{name_user}'")
    result = cursor.fetchone()
    if result:
        if pass_user == result[0]:
            print("Login bem-sucedido!")
            return True
        else:
            print("Senha incorreta. Tente novamente.")
            return False
    else:
        print("Usuário não encontrado. Verifique o nome de usuário.")



#cadastro de usuario
def cadastrar_usuario(name_user, pass_user):
    cursor = connection.cursor()

    
    cursor.execute("SELECT * FROM USUARIOS WHERE name_user = %s", (name_user,))
    existing_user = cursor.fetchone()

    if existing_user:
        print(f"Usuário com o nome {name_user} já existe. Por favor, escolha outro nome.")
        return False
    else:
        
        insert_query = "INSERT INTO USUARIOS (name_user, pass_user) VALUES (%s, %s)"
        user_data = (name_user, pass_user)
        cursor.execute(insert_query, user_data)
        connection.commit()
        print("Usuário cadastrado com sucesso!")
        return True
        
data = "2023-11-20"

#read para aparecer as informações na tela
def read(name):
    cmd = f'select * from vendas where name_user = "{name}";'
    cursor.execute(cmd)
    slct = cursor.fetchall()
    return slct



#cadastro de vendas
def insert(valor, name, prod):
    cmd = f'insert vendas(valor_venda, data_venda, name_user, name_prod) values ({valor}, "{data}", "{name}", "{prod}")'
    cursor.execute(cmd)
    connection.commit()

def delete(id, nome_usuario):
    cmd = f'delete from vendas where id_venda = {id} and name_user = "{nome_usuario}"'
    cursor.execute(cmd)
    connection.commit()


#soma dos valores
def soma(name):
    suma = 0
    cmd = f'select vendas.valor_venda from vendas where name_user = "{name}";'
    cursor.execute(cmd)
    result = cursor.fetchall()
    for i in result:
        suma += i[0]
    return suma

