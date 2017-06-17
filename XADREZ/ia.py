from tabuleiro import *
from peca import *
from node import *
import copy
import random
import time
class Ia:

    tabuleiro = None
    tabuleiroAuxiliar = None
    tipo = None
    cor = None
    listPecasIA = []
    listPecasInimigo = []

    def __init__(self,tabuleiro,tipo,cor):
        self.tabuleiro = tabuleiro
        self.tabuleiroAuxiliar = tabuleiro
        self.tipo = tipo
        self.cor = cor
        self.listPecasIA = []
        self.listPecasInimigo = []
        for i in range(0,8):
            for j in range(0,8):
                if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                    if(self.tabuleiroAuxiliar.matriz[i][j].cor == self.cor):
                        self.listPecasIA.append(self.tabuleiroAuxiliar.matriz[i][j])
                    else:
                        self.listPecasInimigo.append(self.tabuleiroAuxiliar.matriz[i][j])


    def buildTree(self,tipo):
        #print ("Lista Amigo: ",self.listPecasIA)
        #print ("Lista Inimigo: ",self.listPecasInimigo)
        #return

        if(tipo == "max"):
            jogadasPossiveis = []
            poolJogadas = []
            #print("peças IA: ",len(self.listPecasIA))
            for k in range (0,len(self.listPecasIA)):
                #print("Linha: ",self.listPecasIA[k].linha, " Coluna: ", self.listPecasIA[k].coluna, " tipo: ",self.listPecasIA[k].tipo)
                if(self.listPecasIA[k].tipo == "peao"):
                    self.tabuleiroAuxiliar.selecao = self.listPecasIA[k]
                    self.tabuleiroAuxiliar.movimento_peao()
                    self.tabuleiroAuxiliar.defineAlvos()
#                    bestNode = node(-1,None,None)
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel" or self.tabuleiroAuxiliar.matriz[i][j].alvo == True):
                                    coluna = self.listPecasIA[k].coluna
                                    linha = self.listPecasIA[k].linha
                                    if self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel":
                                        valor = 0
                                    elif self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        valor = self.tabuleiroAuxiliar.matriz[i][j].value
                                    novoNo = node(valor,linha,coluna,i,j)
                                    if self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        novoNo.pecaComida = self.tabuleiroAuxiliar.matriz[i][j]
                                    jogadasPossiveis.append(novoNo)

                    #limpando disponiveis e alvos
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel"):
                                    self.tabuleiroAuxiliar.matriz[i][j] = "vazio"
                                else:
                                    self.tabuleiroAuxiliar.matriz[i][j].alvo = False
                if (self.listPecasIA[k].tipo == "bispo"):
                    self.tabuleiroAuxiliar.selecao = self.listPecasIA[k]
                    self.tabuleiroAuxiliar.movimento_bispo()
                    #                    bestNode = node(-1,None,None)
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel" or self.tabuleiroAuxiliar.matriz[i][j].alvo == True):
                                    coluna = self.listPecasIA[k].coluna
                                    linha = self.listPecasIA[k].linha
                                    if self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel":
                                        valor = 0
                                    elif self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        valor = self.tabuleiroAuxiliar.matriz[i][j].value
                                    novoNo = node(valor,linha,coluna,i,j)
                                    if self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        novoNo.pecaComida = self.tabuleiroAuxiliar.matriz[i][j]
                                    jogadasPossiveis.append(novoNo)

                    #limpando disponiveis e alvos
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel"):
                                    self.tabuleiroAuxiliar.matriz[i][j] = "vazio"
                                else:
                                    self.tabuleiroAuxiliar.matriz[i][j].alvo = False
                if (self.listPecasIA[k].tipo == "torre"):
                    self.tabuleiroAuxiliar.selecao = self.listPecasIA[k]
                    self.tabuleiroAuxiliar.movimento_torre()
                    #                    bestNode = node(-1,None,None)
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel" or self.tabuleiroAuxiliar.matriz[i][j].alvo == True):
                                    coluna = self.listPecasIA[k].coluna
                                    linha = self.listPecasIA[k].linha
                                    if self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel":
                                        valor = 0
                                    elif self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        valor = self.tabuleiroAuxiliar.matriz[i][j].value
                                    novoNo = node(valor,linha,coluna,i,j)
                                    if self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        novoNo.pecaComida = self.tabuleiroAuxiliar.matriz[i][j]
                                    jogadasPossiveis.append(novoNo)

                    #limpando disponiveis e alvos
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel"):
                                    self.tabuleiroAuxiliar.matriz[i][j] = "vazio"
                                else:
                                    self.tabuleiroAuxiliar.matriz[i][j].alvo = False
                if (self.listPecasIA[k].tipo == "cavalo"):
                    self.tabuleiroAuxiliar.selecao = self.listPecasIA[k]
                    self.tabuleiroAuxiliar.movimento_cavalo()
                    #                    bestNode = node(-1,None,None)
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel" or self.tabuleiroAuxiliar.matriz[i][j].alvo == True):
                                    coluna = self.listPecasIA[k].coluna
                                    linha = self.listPecasIA[k].linha
                                    if self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel":
                                        valor = 0
                                    elif self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        valor = self.tabuleiroAuxiliar.matriz[i][j].value
                                    novoNo = node(valor,linha,coluna,i,j)
                                    if self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        novoNo.pecaComida = self.tabuleiroAuxiliar.matriz[i][j]
                                    jogadasPossiveis.append(novoNo)

                    #limpando disponiveis e alvos
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel"):
                                    self.tabuleiroAuxiliar.matriz[i][j] = "vazio"
                                else:
                                    self.tabuleiroAuxiliar.matriz[i][j].alvo = False
                if (self.listPecasIA[k].tipo == "rainha"):
                    self.tabuleiroAuxiliar.selecao = self.listPecasIA[k]
                    self.tabuleiroAuxiliar.movimento_bispo()
                    self.tabuleiroAuxiliar.movimento_torre()
                    #                    bestNode = node(-1,None,None)
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel" or self.tabuleiroAuxiliar.matriz[i][j].alvo == True):
                                    coluna = self.listPecasIA[k].coluna
                                    linha = self.listPecasIA[k].linha
                                    if self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel":
                                        valor = 0
                                    elif self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        valor = self.tabuleiroAuxiliar.matriz[i][j].value
                                    novoNo = node(valor,linha,coluna,i,j)
                                    if self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        novoNo.pecaComida = self.tabuleiroAuxiliar.matriz[i][j]
                                    jogadasPossiveis.append(novoNo)

                    #limpando disponiveis e alvos
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel"):
                                    self.tabuleiroAuxiliar.matriz[i][j] = "vazio"
                                else:
                                    self.tabuleiroAuxiliar.matriz[i][j].alvo = False
                if (self.listPecasIA[k].tipo == "rei"):
                    self.tabuleiroAuxiliar.selecao = self.listPecasIA[k]
                    self.tabuleiroAuxiliar.movimento_rei(self.tabuleiroAuxiliar.selecao.linha,self.tabuleiroAuxiliar.selecao.coluna)
                    #                    bestNode = node(-1,None,None)
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel" or self.tabuleiroAuxiliar.matriz[i][j].alvo == True):
                                    coluna = self.listPecasIA[k].coluna
                                    linha = self.listPecasIA[k].linha
                                    if self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel":
                                        valor = 0
                                    elif self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        valor = self.tabuleiroAuxiliar.matriz[i][j].value
                                    novoNo = node(valor,linha,coluna,i,j)
                                    if self.tabuleiroAuxiliar.matriz[i][j].alvo == True:
                                        novoNo.pecaComida = self.tabuleiroAuxiliar.matriz[i][j]
                                    jogadasPossiveis.append(novoNo)
                    #limpando disponiveis e alvos
                    for i in range (0,8):
                        for j in range (0,8):
                            if(self.tabuleiroAuxiliar.matriz[i][j] != "vazio"):
                                if(self.tabuleiroAuxiliar.matriz[i][j].tipo == "disponivel"):
                                    self.tabuleiroAuxiliar.matriz[i][j] = "vazio"
                                else:
                                    self.tabuleiroAuxiliar.matriz[i][j].alvo = False
            print("Numero de jogadas: ",len(jogadasPossiveis))
            #escolhendo melhores jogadas podendo ter mais de uma com o mesmo peso
            #caso tenham mais de uma sera aleatoria a escolha
            #deixando a IA menos previsivel
            maiorValor = jogadasPossiveis[0].cost
            poolJogadas.append(jogadasPossiveis[0])
            for i in range (1,len(jogadasPossiveis)):
                if jogadasPossiveis[i].cost == maiorValor:
                    poolJogadas.append(jogadasPossiveis[i])
                if jogadasPossiveis[i].cost > maiorValor:
                    maiorValor = jogadasPossiveis[i].cost
                    poolJogadas.clear()
                    poolJogadas.append(jogadasPossiveis[i])
            print("numero pool: ",len(poolJogadas))
            pos = random.randint(0,len(poolJogadas) - 1)
            print("random: ",pos)
            #realiza jogada do node pos

            #joga jogada realizada para buildtree 'mini'
            self.buildTree("mini")

            #desfaz a jogada caso necessário
            return poolJogadas[pos]

        #se achar valor 200 significa que comeu o rei, então para o algoritmo!!!
        elif(tipo == "mini"):
            return

        return


    def movePecas(self,node):
        self.tabuleiroAuxiliar.matriz[node.linhaNova][node.colunaNova] = self.tabuleiroAuxiliar.matriz[node.linhaAntiga][node.colunaAntiga]
        self.tabuleiroAuxiliar.matriz[node.linhaAntiga][node.colunaAntiga] = "vazio"
        self.tabuleiroAuxiliar.matriz[node.linhaNova][node.colunaNova].coluna = node.colunaNova
        self.tabuleiroAuxiliar.matriz[node.linhaNova][node.colunaNova].linha = node.linhaNova
        if node.cost > 0:
            return True
        else:
            return False


    def realizaJogada(self,tipo):
        node = self.buildTree(tipo)
        time.sleep(0.4)
        return self.movePecas(node)


