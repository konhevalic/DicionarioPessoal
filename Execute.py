import Words

def chooseOption():
    print("O que deseja fazer?\n"
          "[ 1 ] Adicionar\n"
          "[ 2 ] Consultar uma palavra\n"
          "[ 3 ] Consultar todo o dicionário\n"
          )

    option = int(input('Digite a opção desejada: '))

    if option == 1:
        word = input("Palavra a ser adicionada: ")
        meaning = input("Seu significado: ")
        Words.add_word(f'{word}', f'{meaning}')

    if option == 2:
        word = input("Qual palavra deseja consultar? ")
        Words.search_word(word)

    if option == 3:
        Words.show_all()


def continueProgram():
    print("Deseja continuar? \n"
          "[ S ] sim \n"
          "[ N ] não")

    option = (input('Digite a opção desejada: '))

    if option == "S":
        chooseOption()
    else:
        print("Programa encerrado!")


