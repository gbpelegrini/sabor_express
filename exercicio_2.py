import os

def impar_par():
    num = int(input('Digite um número: '))
    os.system('cls')

    if num % 2 == 1:
        print(f'{num} é um número ímpar')
    else:
        print(f'{num} é um número par')

def idade():
    idade_user = int(input('Digite sua idade: '))
    os.system('cls')

    if idade_user <= 12:
        print('Você é uma criança')
    elif 12 < idade_user <= 18:
        print('Você é um adolescente')
    else:
        print('Você é um adulto')

def usuario_senha():
    usuario_padrao = 'gbpelegrini'
    senha_padrao = '@sterix'

    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')
    os.system('cls')

    if usuario_padrao == usuario and senha_padrao == senha:
        print('Login com sucesso!')
    else:
        print('Senha ou usuário incorreto.')

def quadrante():
    x = float(input("Digite a coordenada x: "))
    y = float(input("Digite a coordenada y: "))
    os.system('cls')

    if x > 0 and y > 0:
        print("O ponto está no primeiro quadrante.")
    elif x < 0 and y > 0:
        print("O ponto está no segundo quadrante.")
    elif x < 0 and y < 0:
        print("O ponto está no terceiro quadrante.")
    elif x > 0 and y < 0:
        print("O ponto está no quarto quadrante.")
    else:
        print("O ponto está sobre um eixo ou na origem.")

def main():
    quadrante()

if __name__ == '__main__':
    main()