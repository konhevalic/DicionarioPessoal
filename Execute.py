import math
import Words

def showOptions():
    print("O que deseja fazer?\n"
          "[ 1 ] Adicionar\n"
          "[ 2 ] Consultar uma palavra\n"
          "[ 3 ] Consultar todo o dicionário\n"
          )

def startProgram():
    showOptions()

    option = input('Digite a opção desejada: ')

    while option.isalpha():
        showOptions()
        option = input('Digite a opção desejada: ')

    while option == '':
        showOptions()
        option = input('Digite a opção desejada: ')

    option = int(option)
    chooseOption(option)

def addWord(word, meaning):
    if word != '' and meaning != '':
        Words.add_word(f'{word}', f'{meaning}')
        continueProgram()
    else:
        return "Oops... Insira um valor diferente de vazio"

def conferWord(word):
    if word != '':
        Words.search_word(word)
        continueProgram()
    else:
        return "Oops... Insira um valor diferente de vazio"


def chooseOption(option):
    if option == 1:
        word = input("Palavra a ser adicionada: ")
        meaning = input("Seu significado: ")
        addWord(word, meaning)

    elif option == 2:
        word = input("Qual palavra deseja consultar? ")
        conferWord(word)

    elif option == 3:
        Words.show_all()
        continueProgram()
    elif option == '':
        return "Oops... Insira um valor entre 1 e 3"
    else:
        return "Oops... Insira um número válido"

def selectOptionToContinueProgram(option):
    if option == "S" or option == "s":
        startProgram()
    elif option == "N" or option == "n":
        print("Programa encerrado!")
    else:
        return "Oops... Insira uma resposta válida"

def continueProgram():
    print("Deseja continuar? \n"
          "[ S ] sim \n"
          "[ N ] não")

    option = (input('Digite a opção desejada: '))

    selectOptionToContinueProgram(option)


def test_deve_falhar_quando_numero_menor_1():
    assert chooseOption(0) == "Oops... Insira um número válido"

def test_deve_falhar_quando_numero_maior_3():
    assert chooseOption(5) == "Oops... Insira um número válido"

def test_deve_falhar_quando_texto():
    assert chooseOption('abc') == "Oops... Insira um número válido"

def test_deve_falhar_quando_input_vazio():
    assert chooseOption('') == "Oops... Insira um valor entre 1 e 3"
    assert selectOptionToContinueProgram('') == "Oops... Insira uma resposta válida"
    assert addWord('', '') == "Oops... Insira um valor diferente de vazio"
    assert addWord('', 'meaning of the word') == "Oops... Insira um valor diferente de vazio"
    assert addWord('word', '') == "Oops... Insira um valor diferente de vazio"
    assert conferWord('') == "Oops... Insira um valor diferente de vazio"

def test_deve_falhar_quando_input_diferente_S():
    assert selectOptionToContinueProgram('A') == "Oops... Insira uma resposta válida"

def test_deve_falhar_quando_input_diferente_s():
    assert selectOptionToContinueProgram('a') == "Oops... Insira uma resposta válida"

def test_deve_falhar_quando_input_diferente_N():
    assert selectOptionToContinueProgram('M') == "Oops... Insira uma resposta válida"

def test_deve_falhar_quando_input_diferente_n():
    assert selectOptionToContinueProgram('m') == "Oops... Insira uma resposta válida"

