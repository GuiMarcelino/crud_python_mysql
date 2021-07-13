# python e Mysql
# Criar um Crud simples, usando funções ou orientação a objetos
# cada operação deve estar isolada(uma função para cada operação)
# validar os cmapos e não ter informações duplicada (validar pelo CPF),
# cadastro de contatos.

#ID (PRIMARY KEY AUTO _INCREMENT), NOME, SOBRENOME, CPF (UNIQUE), EMAIL, TELEFONE

from funcoes import  alter, insert, select_all, select_id
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    database= 'CADASTRO_CONTATO',
    user= 'root',
    password='Gui281209'
)


while True:
    print('=============================================')
    print('           CADASTRO DE CONTATOS')
    print('=============================================')
    print('')
    opcao = input('LISTA DE COMANDOS.\n'
    '[1] - INSERIR CONTATO\n'
    '[2] - ALTERAR CONTATO\n'
    '[3] - LISTAR TODOS OS CONTATOS\n'
    '[4] - BUSCAR CONTATO POR ID\n'
    '[5] - DELETAR CONTATO\n'
    '[6] - FINALIZAR CADASTRO\n'
    'Informe a opção desejada => ')
    
    if opcao == '1':
        insert(db)

    elif opcao =='2':
        alter(db)

    elif opcao == '3':
        select_all(db)

    elif opcao == '4':
        select_id(db)





