import numpy as np
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def showOptions(lista):
    for i, cat in enumerate(lista,1):
         print(f'   {i}. {cat}')
    print('='*50)
    


def menuDebitar():
    limpar_terminal()
    print('='*50)
    print("""||     Selecione Categoria da dispesa ||""")
    print('='*50)
    
    categories = ['Comida', 'Contas', 'Lazer', 'Viagens'] #aqui vai puxar essas categoria do banco de dados
    showOptions(categories)
    opcao = int(input('Select: '))
    valor = float(input('Valor: '))
    # debitar(categoria = categories[opcao-1], valor=float )
    menu()

def menuCreditar():
    limpar_terminal()
    print('='*50)
    print("""||            Selecione sua opção               ||""")
    print('='*50)
    
    categoriesDeb = ['Comida', 'Contas', 'Lazer', 'Viagens'] #assim como na parte de debito aqui vai ser puxado de um banco de dados
                                                            # para adicionar a opção de reembolsos
    categories = ['Salario', 'Vendas', 'Bonus', 'Reembolso' ]
    showOptions(categories)
    opcao = int(input('Select: '))
    if categories[opcao-1] == 'Reembolso':
        showOptions(categoriesDeb)
        
        
    
def menu():
    limpar_terminal()
    print('='*50)
    print("""||            Selecione sua opção               ||""")
    print('='*50)
    print("   1. Creditar")
    print("   2. Debitar")
    print("   3. Sair")
    print('='*50)
    opcao = int(input('Select: '))
    
    match opcao:
        case 1:
            menuCreditar()
        case 2:
            menuDebitar()
        case 3:
            print('oi')
            #sair
        

