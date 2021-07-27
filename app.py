
from funcoes import *
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    database= 'CADASTRO_CONTATO',
    user= 'root',
    password='Gui281209'
)


while True:
    print('==============================================')
    print('           CADASTRO DE CONTATOS')
    print('==============================================')
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
        update(db)

    elif opcao == '3':
        select_all(db)

    elif opcao == '4':
        select_id(db)

    elif opcao == '5':
        delete(db)

    elif opcao == '6':
         exit()





