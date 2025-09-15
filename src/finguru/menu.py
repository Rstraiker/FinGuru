import numpy as np
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def showOptions(lista):
    for i, cat in enumerate(lista,1):
         print(f'   {i}. {cat}')
    print('='*50)

def title(frase):
    print('='*50)
    print('||'+ frase.center(46)+'||')
    print('='*50)


def menuDebitar():
    limpar_terminal()
    title('Selecione Categoria da dispesa')
    categories = ['Comida', 'Contas', 'Lazer', 'Viagens'] #aqui vai puxar essas categoria do banco de dados
    showOptions(categories)
    opcao = int(input('Select: '))
    valor = float(input('Valor: '))
    # debitar(categoria = categories[opcao-1], valor=float )
    menu()

def menuCreditar():
    limpar_terminal()
    title('Selecione Opção de Credito')
    categoriesDeb = ['Comida', 'Contas', 'Lazer', 'Viagens'] #assim como na parte de debito aqui vai ser puxado de um banco de dados
                                                            # para adicionar a opção de reembolsos
    categories = ['Salario', 'Vendas', 'Bonus', 'Reembolso' ]
    showOptions(categories)
    opcao = int(input('Select: '))
    valor = float(input('Valor: '))
    if categories[opcao-1] == 'Reembolso':
        limpar_terminal()
        title('Selecione Opção de Reembolso')
        showOptions(categoriesDeb)
        reembolso = input('Select: ')
        #reembolsar(categoria = categoriesDeb[opcao-1], valor=float )
    else:
        #creditar(categoria = categories[opcao-1], valor)
        print('Valor creditado')
    menu()
    
    
def showStatistics():
    title('Dados gerais')
    # Recebimentos = getRecebimentos()
    # Gastos = getGastos()
    # saldo = getSaldo()
def menu():
    
    opcoes = ['Creditar', 'Debitar', 'Informacoes' ,'Sair']
    limpar_terminal()
    title('Selecione Sua Opção')
    showOptions(opcoes)
    opcao = int(input('Select: '))
    
    match opcao:
        case 1:
            menuCreditar()
        case 2:
            menuDebitar()
        case 3:
            print('oi')
            


