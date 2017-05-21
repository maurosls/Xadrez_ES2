from PPlay.window import *
from PPlay.sprite import *
from peca import *

class Tabuleiro:

    janela = None
    mouse = None

    tamanhoSprite = None
    branco = None
    preto = None
    verde = None
    selecaoSprite = None

    casas = None
    selecao = None

    matriz = None


    def __init__(self):
        self.janela = Window(600,600)
        self.mouse = self.janela.get_mouse()

        self.casas = []
        self.tamanhoSprite = 75
        cor = "preto"
        for i in range(0,8):
            for j in range(0,8):
                if (cor == "preto"):
                    casa = Sprite("Sprites/preto.png")
                    cor = "branco"
                else:
                    casa = Sprite("Sprites/branco.png")
                    cor = "preto"
                casa.x = j * self.tamanhoSprite
                casa.y = i * self.tamanhoSprite
                self.casas.append(casa)
            if (cor == "preto"):
                cor = "branco"
            else:
                cor = "preto"

        self.selecaoSprite = Sprite("Sprites/selecao.png")
        self.selecaoSprite.x = self.janela.width
        self.selecaoSprite.y = self.janela.height

    def inicializaMatriz(self):
        torreP1 = Peca("torre", "preto", Sprite("Sprites/torreP.png"),0,0,False)
        cavaloP1 = Peca("cavalo", "preto", Sprite("Sprites/cavaloP.png"),0,1,False)
        bispoP1 = Peca("bispo", "preto", Sprite("Sprites/bispoP.png"), 0, 2,False)
        rainhaP = Peca("rainha", "preto", Sprite("Sprites/rainhaP.png"), 0, 3,False)
        reiP = Peca("rei", "preto", Sprite("Sprites/reiP.png"), 0, 4,False)
        bispoP2 = Peca("bispo", "preto", Sprite("Sprites/bispoP.png"), 0, 5,False)
        cavaloP2 = Peca("cavalo", "preto", Sprite("Sprites/cavaloP.png"), 0, 6,False)
        torreP2 = Peca("torre", "preto", Sprite("Sprites/torreP.png"), 0, 7,False)
        peaoP1 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"),1,0,False)
        peaoP2 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 1,False)
        peaoP3 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 2,False)
        peaoP4 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 3,False)
        peaoP5 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 4,False)
        peaoP6 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 5,False)
        peaoP7 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 6,False)
        peaoP8 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 7,False)

        torreB1 = Peca("torre", "branco", Sprite("Sprites/torreB.png"),7,0,False)
        cavaloB1 = Peca("cavalo", "branco", Sprite("Sprites/cavaloB.png"),7,1,False)
        bispoB1 = Peca("bispo", "branco", Sprite("Sprites/bispoB.png"), 7, 2,False)
        rainhaB = Peca("rainha", "branco", Sprite("Sprites/rainhaB.png"), 7, 3,False)
        reiB = Peca("rei", "branco", Sprite("Sprites/reiB.png"), 7, 4,False)
        bispoB2 = Peca("bispo", "branco", Sprite("Sprites/bispoB.png"), 7, 5,False)
        cavaloB2 = Peca("cavalo", "branco", Sprite("Sprites/cavaloB.png"), 7, 6,False)
        torreB2 = Peca("torre", "branco", Sprite("Sprites/torreB.png"), 7, 7,False)
        peaoB1 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"),6,0,False)
        peaoB2 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 1,False)
        peaoB3 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 2,False)
        peaoB4 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 3,False)
        peaoB5 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 4,False)
        peaoB6 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 5,False)
        peaoB7 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 6,False)
        peaoB8 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 7,False)

        self.matriz = [[torreP1,cavaloP1,bispoP1,rainhaP,reiP,bispoP2,cavaloP2,torreP2],
       [peaoP1, peaoP2, peaoP3, peaoP4, peaoP5, peaoP6, peaoP7, peaoP8],
       ["vazio", "vazio", "vazio", "vazio", "vazio", "vazio", "vazio", "vazio"],
       ["vazio", "vazio", "vazio", "vazio", "vazio", "vazio", "vazio", "vazio"],
       ["vazio", "vazio", "vazio", "vazio", "vazio", "vazio", "vazio", "vazio"],
       ["vazio", "vazio", "vazio", "vazio", "vazio", "vazio", "vazio", "vazio"],
       [peaoB1, peaoB2, peaoB3, peaoB4, peaoB5, peaoB6, peaoB7, peaoB8],
       [torreB1,cavaloB1,bispoB1,rainhaB,reiB,bispoB2,cavaloB2,torreB2]]

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if (self.matriz[i][j]!='vazio'):
                    self.matriz[i][j].sprite.x = j*self.tamanhoSprite
                    self.matriz[i][j].sprite.y = i*self.tamanhoSprite

    def selecionaPeca(self):
        for i in range(0,len(self.matriz)):
            for j in range(0, len(self.matriz[0])):
                if (self.matriz[i][j]!="vazio"):
                    while (self.mouse.is_button_pressed(1) and
                               self.mouse.is_over_object(self.matriz[i][j].sprite) and self.matriz[i][j].time=="branco" or self.mouse.is_button_pressed(1) and
                               self.mouse.is_over_object(self.matriz[i][j].sprite) and self.matriz[i][j].time=="preto" ):
                        for x in range(0, len(self.matriz)):
                            for y in range(0, len(self.matriz[0])):
                                if (self.matriz[x][y] != "vazio"):
                                    if(self.matriz[x][y].tipo == "disponivel"):
                                        self.matriz[x][y] = "vazio"
                        self.janela.update()
                        self.selecaoSprite.x = self.matriz[i][j].sprite.x
                        self.selecaoSprite.y = self.matriz[i][j].sprite.y
                        self.selecao = self.matriz[i][j]

    def defineDisponiveis(self):
        if (self.selecao!=None):
# ---------------------------------> a partir daqui peoes brancos -------------------------------------------------------------------------------

            if(self.selecao.tipo=="peao" and self.selecao.time=="branco"):
                #Se peça ainda não moveu, liberar duas casas
                if(self.selecao.ja_moveu == False):
                    #self.selecao.ja_moveu = True
                    #Checando se há peças na linha -1
                    if(self.matriz[self.selecao.linha-1][self.selecao.coluna] == "vazio"):
                        disponivel = Peca("disponivel",None,Sprite("Sprites/verde.png"),self.selecao.linha-1,self.selecao.coluna,False)
                        self.matriz[self.selecao.linha-1][self.selecao.coluna] = disponivel
                        #Checando se há peças na linha -2
                        if(self.matriz[self.selecao.linha-2][self.selecao.coluna] == "vazio"):
                            disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), self.selecao.linha -2,self.selecao.coluna,False)
                            self.matriz[self.selecao.linha -2][self.selecao.coluna] = disponivel
                #Se peça já moveu, liberar uma casa
                if(self.selecao.ja_moveu == True):
                    #Checando se está saindo do tabuleiro!
                    if(self.selecao.linha-1 >= 0):
                        if(self.matriz[self.selecao.linha-1][self.selecao.coluna] == "vazio"):
                            disponivel = Peca("disponivel",None,Sprite("Sprites/verde.png"),self.selecao.linha-1,self.selecao.coluna,False)
                            self.matriz[self.selecao.linha-1][self.selecao.coluna] = disponivel
                    else:
                        return
                        #PROGRAMAR A TROCA DE PEÇAS!
                #Colorindo as peças que podem ser comidas
                if self.selecao.linha-1 >= 0:
                    if self.selecao.coluna+1 <= 7:
                        if self.matriz[self.selecao.linha-1][self.selecao.coluna+1] != "vazio":
                            return #pintar o alvo
                    if self.selecao.coluna-1 >= 0:
                        if self.matriz[self.selecao.linha-1][self.selecao.coluna-1] != "vazio":
                            return #pintar o alvo


# --------------------------------------------- a partir daqui para peos pretos -----------------------------------------------------------

            if (self.selecao.tipo == "peao" and self.selecao.time == "preto"):
                # Se peça ainda não moveu, liberar duas casas
                if (self.selecao.ja_moveu == False):
                    # Checando se há peças na linha +1
                    if (self.matriz[self.selecao.linha + 1][self.selecao.coluna] == "vazio"):
                        disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), self.selecao.linha + 1,
                                          self.selecao.coluna, False)
                        self.matriz[self.selecao.linha + 1][self.selecao.coluna] = disponivel
                        # Checando se há peças na linha +2
                        if (self.matriz[self.selecao.linha + 2][self.selecao.coluna] == "vazio"):
                            disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), self.selecao.linha + 2,
                                              self.selecao.coluna, False)
                            self.matriz[self.selecao.linha + 2][self.selecao.coluna] = disponivel
                # Se peça já moveu, liberar uma casa
                if (self.selecao.ja_moveu == True):
                    # Checando se está saindo do tabuleiro!
                    if (self.selecao.linha + 1 < len(self.matriz)):
                        if (self.matriz[self.selecao.linha + 1][self.selecao.coluna] == "vazio"):
                            disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), self.selecao.linha + 1,
                                              self.selecao.coluna, False)
                            self.matriz[self.selecao.linha + 1][self.selecao.coluna] = disponivel
                    else:
                        return
                        # PROGRAMAR A TROCA DE PEÇAS!
                # Colorindo as peças que podem ser comidas
                if self.selecao.linha + 1 < len(self.matriz):
                    if self.selecao.coluna + 1 <= 7:
                        if self.matriz[self.selecao.linha + 1][self.selecao.coluna + 1] != "vazio":
                            return  # pintar o alvo
                    if self.selecao.coluna - 1 >= 0:
                        if self.matriz[self.selecao.linha + 1][self.selecao.coluna - 1] != "vazio":
                            return  # pintar o alvo




    def confirmaMovimento(self):
        update = False
        disponivelSelecionado = None
        for i in range(0,len(self.matriz)):
            for j in range(0, len(self.matriz[0])):
                if (self.matriz[i][j]!="vazio"):
                    while (self.mouse.is_button_pressed(1) and self.mouse.is_over_object(self.matriz[i][j].sprite) and self.matriz[i][j].tipo=="disponivel"):
                        self.janela.update()
                        update = True
                        disponivelSelecionado = self.matriz[i][j]
        if (update==True):
            self.matriz[self.selecao.linha][self.selecao.coluna] = "vazio"
            self.selecao.linha = disponivelSelecionado.linha
            self.selecao.coluna = disponivelSelecionado.coluna
            self.matriz[disponivelSelecionado.linha][disponivelSelecionado.coluna] = self.selecao
            if (self.selecao.tipo=="peao"):
                self.selecao.ja_moveu = True
            self.selecao = None
            self.selecaoSprite.x=self.janela.width
            self.selecaoSprite.y=self.janela.height

            for x in range(0, len(self.matriz)):
                for y in range(0, len(self.matriz[0])):
                    if (self.matriz[x][y] != "vazio"):
                        if (self.matriz[x][y].tipo == "disponivel"):
                            self.matriz[x][y] = "vazio"

    def atualiza(self):
        for i in range(0, len(self.casas)):
            self.casas[i].draw()

        for i in range(0,len(self.matriz)):
            for j in range(0,len(self.matriz[0])):
                if (self.matriz[i][j]!= "vazio"):
                    self.matriz[i][j].sprite.x = j * self.tamanhoSprite
                    self.matriz[i][j].sprite.y = i * self.tamanhoSprite
                    self.matriz[i][j].sprite.draw()


        self.selecaoSprite.draw()

        self.janela.update()
