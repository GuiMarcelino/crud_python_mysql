# python e Mysql
# Criar um Crud simples, validar os campos e não ter informações duplicadas,
# cadastro de contatos.


import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    database= 'CADASTRO',
    user= 'root',
    password='Gui281209'
)
try:
    cursor = db.cursor()
    print('Conectado com sucesso.')
    # comando_sql = 'INSERT INTO CONTATOS (NOME, SOBRENOME, CPF, EMAIL, TELEFONE) VALUES ("Guilherme", "Marcelino", "07193456938", "guilhermemarcelino_91@outlook.com","47991854342" )'
    # comando_sql = 'INSERT INTO CONTATOS (NOME, SOBRENOME, CPF, EMAIL, TELEFONE) VALUES ("Jonathan", "Prange", "09383735681", "jonathan_prange90outlook.com","47991029384" )'
    #comando_sql = 'UPDATE CONTATOS SET NOME = "jonatan" WHERE ID = 1'
    # comando_sql = 'DELETE FROM CONTATOS WHERE ID = 1'
    comando_sql = 'SELECT * FROM CONTATOS'
    cursor.execute(comando_sql)
    resultado = cursor.fetchall()
    for linha in resultado: # mesma coisa que com for index in resultado
        print(f'nome: {linha[1]}\nsobrenome: {linha[2]}\nCPF: {linha[3]}\nemail: {linha[4]}\ntelefone: {linha[5]}\n')
    # db.commit()
    cursor.close()
except:
    print('Não foi possível conectar no banco')

