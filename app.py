import os

restaurantes = ['Abbraccio', 'Outback']

def voltar_ao_menu():
      input('Digite uma tecla para voltar ao menu principal. ')
      main()

def limpar_tela(texto):
      os.system('cls')
      print(texto)
      print()

def opcao_invalida():
      print('Opção inválida\n')
      voltar_ao_menu()

def cadastrar_novo_restaurante():
      limpar_tela('Cadastro de novos restaurantes.')
      nome_restaurante = input('Nome do restaurante: ')
      restaurantes.append(nome_restaurante)
      print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso.')
      voltar_ao_menu()

def listar_restaurante():
      limpar_tela('Listando os restaurantes...')
      for item in restaurantes:
            print(f'+ {item}\n')
      voltar_ao_menu()

def finalizar_app():
      limpar_tela('Finalizando o app.')

def exibir_nome_do_programa():
      print("""
      𝒮𝒶𝒷ℴ𝓇 ℰ𝓍𝓅𝓇ℯ𝓈𝓈
            """)

def exibir_opcoes():
      print('1. Cadastrar Restaurante')
      print('2. Listar Restaurante')
      print('3. Ativar Restaurante')
      print('4. Sair\n')

def escolher_opcao():
      try:
            opcao_escolha = int(input('Escolha uma opção: '))
            print(f'Voce escolheu a opcao: {opcao_escolha}\n')

            if opcao_escolha == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolha == 2:
                  listar_restaurante()
            elif opcao_escolha == 3:
                  print('Ativar Restaurante')
            elif opcao_escolha == 4:
                  finalizar_app()
            else: 
                  opcao_invalida()
      except:
            opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
      main()




