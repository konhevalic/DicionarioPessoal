import sqlite3

# cria a conexão com o banco de dados
connection = sqlite3.connect('wordsTest.db')

# cursor que permite manipular e executar comandos no banco de dados, como consultas
cursor = connection.cursor()

#Criando uma tabela:
cursor.execute("""CREATE TABLE words (
    word text,
    meaning text
    )""")


