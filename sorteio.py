from random import randint

class Pessoa:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

class Escolha:
    def __init__(self, pessoa, email, escolhido):
        self.pessoa = pessoa
        self.email = email
        self.escolhido = escolhido

VINI = Pessoa(0, 'Vinicius', 'vinicius.ruiiz@gmail.com')
GEO = Pessoa(1, 'Geovanna', 'gegepedroso1234@gmail.com')
THI = Pessoa(2, 'Thiago', 'thiago12lopesdeoliveira@gmail.com')
SARAH = Pessoa(3, 'Sarah', 'sarinhamfig54321@gmail.com')
KAUA = Pessoa(4, 'Kaua', 'kakavini360@gmail.com')
BIEL_L = Pessoa(5, 'Gabriel Muita Das Vezes', 'limagabrielde2015@gmail.com')
BIEL_H = Pessoa(6, 'Gabriel Normal', 'gabriel.holanda2006@gmail.com')
ERIK = Pessoa(7, 'Erik', 'eriksilvadeoliveira8@gmail.com')
MARI = Pessoa(8, 'Mariana', 'mariana.fig28@gmail.com')
DUDA = Pessoa(9, 'Eduarda', 'mariafer49@outlook.com.br')
BIA = Pessoa(10, 'Beatriz', 'beatrizromeiro@usp.br')
LEO = Pessoa(11, 'Leonardo', 'leonardobds008@gmail.com')
ALANYS = Pessoa(12, 'Alanys', 'alanyssilvah04@gmail.com')
grupo = [VINI, GEO, THI, SARAH, KAUA, BIEL_L, BIEL_H, ERIK, MARI, DUDA, BIA, LEO, ALANYS]

def filtra_id(lista, id):
    for i in range(len(lista)-1):
        if lista[i].id == id:
            return lista[i]

# objetos que ainda podem ser escolhidas
disponiveis = grupo.copy()

def create_random(id_pessoa):
    opcoes = list() # objetos que podem ser escolhidos pela pessoa em questao
    for indice in range(len(disponiveis)):
        if disponiveis[indice].id != id_pessoa:
            opcoes.append(disponiveis[indice])
    return opcoes[randint(0,len(opcoes)-1)] # retorna o objeto escolhido aleatoriamente

resultado = list()

def sortear():
    for i_pessoa in range(len(grupo)):
        escolhido = create_random(grupo[i_pessoa].id) # objeto escolhido pela pessoa em questao
        # print(f'{grupo[i_pessoa].nome} -> {escolhido.nome}')
        escolha = Escolha(grupo[i_pessoa].nome, grupo[i_pessoa].email, escolhido.nome)
        resultado.append(escolha)
        disponiveis.remove(escolhido) # escolhido não está mais disponível
    return resultado