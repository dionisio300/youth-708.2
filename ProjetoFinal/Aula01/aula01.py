'''
pip install mysql-connector-python
'''
import mysql.connector as my

def conectarBanco():
    conexao = my.connect(
        user='root',
        database='loja',
        password='1234',
        host='localhost'
    )
    return conexao

def insrirDadosBanco(nome,cpf,email,telefone):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    sql = f"insert into clientes (nome, cpf, email, telefone) values ('{nome}','{cpf}','{email}','{telefone}');"
    cursor.execute(sql)
    conexao.commit()
    conexao.close()
    return 'Dado inserido com sucesso!!'

def mostrarDados():
    conexao = conectarBanco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from clientes'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for cliente in resultado:
        print(f'Nome: {cliente['nome']}, E-mail: {cliente['email']}, Telefone: {cliente['telefone']}')
    conexao.close()

def atualizarTelefone(novoTelefone,id):
    conexao = conectarBanco()
    cursor = conexao.cursor(dictionary=True)
    sql = f"update clientes set telefone = '{novoTelefone}' where id = {id};"
    cursor.execute(sql)
    conexao.commit()
    conexao.close()
    return 'Dados atualizados com sucesso!'

def deletarCliente(id):
    conexao = conectarBanco()
    cursor = conexao.cursor(dictionary=True)
    sql = f"delete from clientes where id = {id}"
    cursor.execute(sql)
    conexao.commit()
    conexao.close()
    return 'Cliente deletado com sucesso!'

'''
Inserir dados no Banco de dados
'''
while True:
    op = input('1 - Cadastrar\n2 - ler os dados\n3 - Atualizar\n4 - Deletar\n5 - Sair\n')
    if op == '5':
        print('Saindo...')
        break
    if op == '1':
        nome = input('Nome: ')
        cpf = input('CPF: ')
        email = input('E-mail: ')
        telefone = input('Telefone: ')
        resultado = insrirDadosBanco(nome,cpf,email,telefone)
        print(resultado)
    if op == '2':
        print('Dados no banco:\n')
        mostrarDados()
    if op == '3':
        novoTelefone = input('Telefone: ')
        id = input('ID: ')
        resultado = atualizarTelefone(novoTelefone,id)
        print(resultado)
    if op == '4':
        id = input('ID: ')
        resultado = deletarCliente(id)
        print(resultado)




