import random

class Tabuleiro:
    def __init__(self,n,m,letras):
        self.tabuleiro=[[None for _ in range(m)] for _ in range(n)]
        self.preencher(letras)

def preencher(self, letras):
    for i in range(len(self.tabuleiro)):
        for j in range(len(self.tabuleiro[i])):
            self.tabuleiro[i][j]=random.choice(letras);        

def imprimir(self):
    for linha in self.tabuleiro:
        print(''.join(linha))

