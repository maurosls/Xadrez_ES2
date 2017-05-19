from tabuleiro import *

tab = Tabuleiro()

tab.inicializaMatriz()

while True:

    tab.atualiza()
    tab.selecionaPeca()
    tab.defineDisponiveis()
    tab.atualiza()
    tab.confirmaMovimento()