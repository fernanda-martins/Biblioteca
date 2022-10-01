'''
- devolver um livro  (incrementa a quantidade dele)
- reservar um livro  (imprime na tela a mensagem “Reservado!”).
- a quantidade do livro deve ser suficiente (maior que 0) para
  emprestá-lo ou reservá-lo. O título não está visível fora da classe'''


class Livro:
    def __init__(self, tit, a, q):
        self.__titulo = tit
        self.autor = a
        self.quantidade = q

    def reservar(self):
        if self.quantidade > 0:
            return True
        else:
            return False

    def emprestar(self):
        if self.quantidade > 0:
            self.quantidade -= 1

    def devolver(self):
        self.quantidade += 1

    def mostrar_titulo(self):
        return self.__titulo

#Intervenção com o usuário:

#Cadastro do livro pelo usuário:
livros = []
while True:
    titulo = input('Título: ')
    autor = input('Autor: ')
    qtde = int(input('Quantidade: '))

    while titulo == '' or autor == '' or qtde <= 0:
        print('ERRO - essa entrada não foi computada')
        titulo = input('Título: ')
        autor = input('Autor: ')
        qtde = int(input('Quantidade: '))
    livro = Livro(titulo, autor, qtde) #objeto
    livros.append(livro) #add objetos na lista livros

    resp = input('Continua (S/N)? ').upper()
    if resp != 'S':
        print('Encerrando cadastro de livros...')
        break

#Listagem dos livros cadastrados:
print('\n*** LIVROS CADASTRADOS ***')
for i in range(len(livros)): #percorre qnts livros tem na lista
    print(livros[i].mostrar_titulo(), livros[i].autor, livros[i].quantidade)

#Execução dos métodos para os livros cadastrados:
continuar = 'S'
while continuar == 'S':
    print('\n*** RESERVA DE LIVRO ***')
    livroReserva = input('Forneça o título para reserva: ')
    for i in range(len(livros)):
        if livroReserva in livros[i].mostrar_titulo():
            if livros[i].reservar():
                print('Livro - ', livros[i].mostrar_titulo(), ' - Reservado!')
            else:
                print('Livro - ', livros[i].mostrar_titulo(), 'indisponível!')
        else: #INFORMA SE O LIVRO NAO PERTENCE AO ACERVO
            print('Esse livro não pertence ao acervo')


    print('\n*** EMPRÉSTIMO DE LIVRO ***')
    livroEmpresta = input('Qual o título do livro que quer emprestar? ')
    for i in range(len(livros)):
        if livroEmpresta in livros[i].mostrar_titulo() and livros[i].quantidade > 0:
            livros[i].emprestar()
            print('Livro - ', livros[i].mostrar_titulo(), '- Emprestado!')
            print('Quantidade em estoque: ', livros[i].quantidade)
        else:
            print('Esse livro não pertence ao acervo')

    print('\n*** DEVOLUÇÃO DE LIVROS ***')
    livroDevolve = input('Qual livro quer devolver? ')
    for i in range(len(livros)):
        if livroDevolve in livros[i].mostrar_titulo() and livros[i].quantidade < qtde:
            livros[i].devolver()
            print('Livro - ', livros[i].mostrar_titulo(), '- Devolvido!')
            print('Quantidade em estoque: ', livros[i].quantidade)
        else:
            print('Esse livro não pertence ao acervo') # EVITA DEVOLVER UM LIVRO Q NAO FAZ PARTE DO ACERVO
            break
    continuar = input('\nDeseja continuar?(S/N) ').upper() 


























