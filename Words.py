import sqlite3
import Execute

# cria a conexão com o banco de dados
connection = sqlite3.connect('wordsTest.db')

# cursor que permite manipular e executar comandos no banco de dados, como consultas
cursor = connection.cursor()

# SQL:
def search_word(word):
    connection = sqlite3.connect('wordsTest.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM words")

    cursor_ordenated = sorted(cursor.fetchall())
    for cursor_ordenated in cursor_ordenated:
        if cursor_ordenated[0] == word:
            print(cursor_ordenated[0] + ': ' + cursor_ordenated[1])

    connection.commit()
    connection.close()

    Execute.continueProgram()

def show_all():
    connection = sqlite3.connect('wordsTest.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM words")

    cursor_ordenated = sorted(cursor.fetchall())
    for cursor_ordenated in cursor_ordenated:
        print(cursor_ordenated[0] + ': ' + cursor_ordenated[1])

    connection.commit()
    connection.close()

    Execute.continueProgram()


def add_word(word, meaning):
    connection = sqlite3.connect('wordsTest.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO words VALUES (?, ?)", (word, meaning))
    connection.commit()
    connection.close()

    Execute.continueProgram()
