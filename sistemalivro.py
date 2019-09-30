import mysql.connector

connection = mysql.connector.connect(host='localhost',user='root',password='',database='mysql',charset='utf8')
cursor = connection.cursor(dictionary=True)
for i in range(2):
    id_livro = input('Digite o codigo do livro')
    nome = input('Digite o nome do livro')
    autor = input('Digite o autor')
    genero = input('Digite o genero do livro')
    editora = input('Digite o nome da editora')
    cursor.execute("INSERT INTO livros(id_livro,nome,autor,genero,editora)VALUES({},{},{},{},{})".format(id_livro,nome,autor,genero,editora))
    connection.commit()

nome = input('Digite o nome que quer deletar')  
cursor.execute("DELETE from livros where nome='{}'".format(nome))
connection.commit()  
