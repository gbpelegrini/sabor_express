import os

pessoas = [
    {'nome':'Guilherme', 'idade':45, 'cidade':'Brasília'},
    {'nome':'Marcos', 'idade':70, 'cidade':'Uberlândia'},
    {'nome':'Karina', 'idade':46, 'cidade':'Brasília'}
]

def imprimir():
    for pessoa in pessoas:
        print(f'{pessoa}')
    print('\n')


def alternar_idade():
    for pessoa in pessoas:
        if pessoa['nome'] == 'Guilherme':
            pessoa['idade'] = 36

def incluir_campo():
    for pessoa in pessoas:
        if pessoa['nome'] == 'Guilherme':
            pessoa['profissao'] = 'Servidor Púbico'

def deletar_campo():
    for pessoa in pessoas:
        if pessoa['nome'] == 'Guilherme':
            del pessoa['cidade']

def main():
    os.system('cls')
    imprimir()
    alternar_idade()
    imprimir()
    incluir_campo()
    imprimir()
    deletar_campo()
    imprimir()

if __name__ == '__main__':
    main()