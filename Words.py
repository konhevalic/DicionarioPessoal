import sqlite3

# cria a conexão com o banco de dados
connection = sqlite3.connect('wordsTest.db')

# cursor que permite manipular e executar comandos no banco de dados, como consultas
cursor = connection.cursor()

#Criando uma tabela:

#cursor.execute("""CREATE TABLE words (
#    word text,
#    meaning text
#    )""")


# SQL:
def show_all():
    connection = sqlite3.connect('wordsTest.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM words")

    cursor_ordenated = sorted(cursor.fetchall())
    for cursor_ordenated in cursor_ordenated:
        print(cursor_ordenated[0] + ': ' + cursor_ordenated[1])

    connection.commit()
    connection.close()


def add_word(word, meaning):
    connection = sqlite3.connect('wordsTest.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO words VALUES (?, ?)", (word, meaning))
    connection.commit()
    connection.close()
