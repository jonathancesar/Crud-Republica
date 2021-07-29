# -*- coding: utf-8 -*-


# imported libraries
import os
import pymysql
from time import sleep
from datetime import date 
import csv

try: # connection
    connection = pymysql.connect(host = 'localhost', database = 'mybdrepu', user = 'root', passwd = '102030')
    cursor = connection.cursor()
    print('')
    print('\033[0;32mCONEXÃO ESTABELECIDA COM SUCESSO!\033[m')
    established = 1
    sleep(2)
    os.system('cls')
except:
    print('')
    print('\033[0;31mERRO AO CONECTAR COM O BANCO DE DADOS...\033[m')
    sleep(1)
    established = 0

if established == 1: # if connection is established

    try:
        while True:
            os.system('cls')
            print('')
            print('CRUD - REPÚBLICA')
            print('')
            menu = ['VISUALIZAR LISTA', 'ADICIONAR REGISTRO', 'ALTERAR REPÚBLICA', 'EXCLUIR REPÚBLICA']
            for index, listItems in enumerate(menu):
                print(f'\033[0;36m[{index + 1}]\033[m {listItems}')
            print('\033[0;31m[0]\033[m SAIR DO PROGRAMA')
            print('')
            selectOption = int(input('SELECIONE A OPÇÃO DESEJADA: '))

            if selectOption in [0, 1, 2, 3, 4, 5]: # Opções

                if selectOption == 1: # Visualizar Lista
                    os.system('cls')
                    print('')
                    try:
                        result = cursor.execute('SELECT * FROM republica')
                        for result in cursor:
                            print(result)
                    except:
                        print('\033[0;31mTABELA NÃO ENCONTRADA VERIFICAR CONEXÃO\033[m')
                    print('')
                    recordBreak = str(input('\033[0;33mPressione ENTER ou qualquer tecla para sair...\033[m '))


                if selectOption == 2: # Adicionar novo Registro de Republica
                    os.system('cls')
                    print('')
                    print('PREENCHA PARA ADICIONAR UM NOVO REGISTRO...')
                    print('')
                    # idRep = str(input('DIGITE O ID:'))
                    nome = str(input('NOME DA REPÚBLICA: '))
                    endereco = str(input('ENDEREÇO: '))

                    print('')
                    confirmInclusion = str(input('CONFIRMAR INCLUSÃO DE REGISTRO? \033[0;31m[Y/N]\033[m? ')).strip().upper()
                    if confirmInclusion == 'Y':
                        try:
                            cursor.execute("INSERT INTO republica (nome, endereco)\
                                            VALUES (%s, %s)", (nome, endereco))
                            connection.commit()
                            print('')
                            print('\033[0;32mINCLUSÃO REALIZADA COM SUCESSO!\033[m')
                        except:
                            print('')
                            print('\033[0;31mINCLUSÃO NÃO REALIZADA, VERIFIQUE A CONEXÃO\033[m')
                    else:
                        print('')
                        print('\033[0;31mINCLUSÃO NÃO REALIZADA\033[m')
                    print('')
                    sleep(2)

                if selectOption == 3: # ALTERAR REPÚBLICA
                    os.system('cls')
                    print('')
                    idRep = int(input('DIGITE O ID PARA ALTERAR O REGISTRO: '))
                    print('')
                    print('PROCURANDO REGISTRO...')
                    print('')
                    sleep(2)
                    try:
                        ProcuraridRep = cursor.execute(f'SELECT * FROM republica WHERE idRep = {idRep}')
                        connection.commit()
                        resultChangeSearch = cursor.fetchone()
                        if resultChangeSearch == None:
                            print('\033[0;31mREGISTRO NÃO ENCONTRADO\033[m')
                            idRepConnection = 0
                        else:
                            print(resultChangeSearch)
                            idRepConnection = 1
                    except:
                        print('\033[0;31mREGISTRO NÃO ENCONTRADO, VERIFIQUE SUA CONEXÃO\033[m')
                        idRepConnection = 0
                    if idRepConnection == 1:
                        print('')
                        listOptions = ['idRep','nome','endereco']
                        for index, listItems in enumerate(listOptions):
                            print(f'\033[0;36m[{index + 1}]\033[m {listItems}')
                        print('')
                        changeColumn = int(input('SELECIONE O NÚMERO QUE DESEJA ALTERAR: '))
                        if changeColumn == 1:
                            changeColumn = 'idRep'
                        elif changeColumn == 2:
                            changeColumn = 'nome'
                        elif changeColumn == 3:
                            changeColumn = 'endereco'
                        print('')
                        newChange = str(input('DIGITE O NOVO VALOR: '))
                        try:
                            changeModify = cursor.execute(f"UPDATE republica SET {changeColumn} = '{newChange}' WHERE idRep = {idRep}")
                            connection.commit()
                            print('')
                            print('\033[0;32mALTERAÇÃO REALIZADA COM SUCESSO!\033[m')
                        except:
                            print('')
                            print('\033[0;31mERRO AO MODIFICAR, VERIFIQUE SUA CONEXÃO\033[m')
                    print('')
                    sleep(2)

                if selectOption == 4: # DETELAR REGISTRO
                    os.system('cls')
                    print('')
                    idRep = int(input('DIGITE O ID QUE DESEJA EXCLUIR: '))
                    print('')
                    try:
                        idRep = cursor.execute(f'SELECT * FROM republica WHERE idRep = {idRep}')
                        connection.commit()
                        resultDeleteSearch = cursor.fetchone()
                        deleteRecordConnection = 1
                        if resultDeleteSearch == None:
                            deleteRecordConnection = 0
                            print('\033[0;31mREGISTRO NÃO ENCONTRADO, VERIFIQUE A LISTA\033[m')
                        else:
                            print(resultDeleteSearch)
                            print('')
                    except:
                        deleteRecordConnection = 0
                        print('\033[0;31mREGISTRO NÃO ENCONTRADO, VERIFIQUE SUA ENTRADA OU CONEXÃO\033[m')
                    if deleteRecordConnection == 1:
                        confirmDelete = str(input('DESEJA REALMENTE EXCLUIR ESTE REGISTRO? \033[0;31m[Y/N]\033[m ')).strip().upper()
                        if confirmDelete == 'Y':
                            try:
                                idRep= cursor.execute(f'DELETE FROM republica WHERE idRep = {idRep}')
                                connection.commit()
                                print('')
                                print('\033[0;32mREGISTRO EXCLUÍDO COM SUCESSO\033[m')
                            except:
                                print('')
                                print('\033[0;31mERROR AO EXCLUIR REGISTRO, VERIFIQUE A CONEXÃO\033[m')
                        else:
                            print('')
                            print('\033[0;31mREGISTRO NÃO EXCLUÍDO\033[m')
                    print('')
                    sleep(2)
                

                if selectOption == 0: # exit program
                    print('')
                    print('\033[0;31mFINALIZAR PROGRAMA\033[m')
                    print('')
                    sleep(1)
                    break
                
            else: # invalid option
                print('')
                print('\033[0;31mOPÇÃO INVALIDA, TENTE NOVAMENTE\033[m')
                sleep(1)

    except KeyboardInterrupt:
        print('\033[0;33mPROGRAMA ENCERRADO PELO USUÁRIO!\033[m')
        print('')
        
elif established == 0: # if connection is not established
        print('')
        print('\033[0;31mVERIFIQUE A CONEXÃO DA BASE DE DADOS E TENTE NOVAMENTE\033[m')
        print('')
