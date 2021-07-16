
def insert(db):
    
    print('Vamos adicionar um contato!!!')
    print(' ')
    nome = input('Informe o nome: ')
    sobrenome = input('sobrenome: ')
    cpf = input('CPF: ')
    email = input('Email: ')
    telefone = input('Telefone: ')
    comando_sql = "INSERT INTO CONTATOS (NOME, SOBRENOME, CPF, EMAIL, TELEFONE) VALUES (%s,%s,%s,%s,%s)"
    valores = (nome, sobrenome, cpf, email, telefone)
    try:
        cursor = db.cursor()
        cursor.execute(comando_sql, valores)
        db.commit()
        cursor.close()
        print(' novo contato inserido !!!')
    except:
        print('Contato não inserido.')

def update(db):
    print('Alterar Contato.')
    print('')
    try:
        nome, sobrenome, cpf, email, telefone = select_id(db)
        id_update = int(input('Selecione o ID que deseja alterar:'))
        alterar_campo = input('Selecione o campo que deseja alterar: ')
        valor_alterado = input(f'Insira um novo dado no campo {alterar_campo}: ')
        if alterar_campo == 'NOME':
            nome = valor_alterado
        elif alterar_campo == 'SOBRENOME':
            sobrenome = valor_alterado
        elif alterar_campo == 'CPF':
            alterar_campo =  valor_alterado
        elif alterar_campo == 'EMAIL':
            alterar_campo = valor_alterado
        elif alterar_campo == 'TELEFONE':
            alterar_campo = valor_alterado
        cursor = db.cursor()
        comando_sql = "UPDATE CONTATOS SET NOME = %s, SOBRENOME = %s, cpf = %s, email = %s, telefone = %s WHERE ID = %s"
        parametros = (nome, sobrenome, cpf, email, telefone, id_update)
        cursor.execute(comando_sql, parametros)
        db.commit()
        cursor.close()
        registro = select_id(db)
        print(f'ID: {registro[0]}\n'
            f'Nome: {registro[1]}\n'
            f'Sobrenome: {registro[2]}\n'
            f'CPF: {registro[3]}\n'
            f'email: {registro[4]}\n'
            f'telefone: {registro[5]}')
        print('')
        cursor.close()

    except:
        print('Não foi possivel alterar o contato.')

def select_all(db):
    print('Lista de contatos')   
    print('')
    try:
        cursor = db.cursor()
        comando_sql = "SELECT * FROM CONTATOS"
        cursor.execute(comando_sql)
        resultado = cursor.fetchall()
        for registro in resultado:
            print(f'ID: {registro[0]}\n'
            f'Nome: {registro[1]}\n'
            f'Sobrenome: {registro[2]}\n'
            f'CPF: {registro[3]}\n'
            f'email: {registro[4]}\n'
            f'telefone: {registro[5]}')
            print('===================================')
            print('')
        cursor.close()

    except:
        print('Não foi possivel visualizar os contatos.')

def select_id(db):
    try: 
        id_contato = int(input('Informe o número do ID que deseja visualizar: '))
        cursor = db.cursor()
        comando_sql = f"SELECT * FROM CONTATOS WHERE ID = {id_contato}"
        cursor.execute(comando_sql)
        registro = cursor.fetchone()
        print(f'ID: {registro[0]}\n'
            f'Nome: {registro[1]}\n'
            f'Sobrenome: {registro[2]}\n'
            f'CPF: {registro[3]}\n'
            f'email: {registro[4]}\n'
            f'telefone: {registro[5]}')
        print('')
        cursor.close()
        return registro
        
    except:
        print('Não foi possivel visualiza o contato.')


def delete(db):
    try:
        id_contato_delete = int(input('Informe o ID do contato que deseja deletar: '))
        cursor = db.cursor()
        comando_sql = f"DELETE FROM CONTATOS WHERE ID = {id_contato_delete}"
        cursor.execute(comando_sql)
        db.commit()
        cursor.close()
        print(f'Contato com ID: {id_contato_delete} excluido com sucesso')
        

    except:
        print('Não foi possivel deletar o contato.')

def exit():
    try:
        return print('Cadastros finalizados!!!')

    except:
        print('Não foi possivél finalizar o Cadastro')

        
    


    
