class livros:
    def __init__(self,nome,genero,autor):
        self.nome = nome
        self.genero = genero
        self.autor = autor

livro1 = livros('Folhas Secas','Romance','Graciliano Ramos')
livro2 = livros('As Aventuras de Jhon','Suspense','Rubens Motta') 
livro3 = livros('Faroeste Caboclo','Terror','Joseph Alencar')

print(livro2)
