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
        torreP1 = Peca("torre", "preto", Sprite("Sprites/torreP.png"),0,0)
        cavaloP1 = Peca("cavalo", "preto", Sprite("Sprites/cavaloP.png"),0,1)
        bispoP1 = Peca("bispo", "preto", Sprite("Sprites/bispoP.png"), 0, 2)
        rainhaP = Peca("rainha", "preto", Sprite("Sprites/rainhaP.png"), 0, 3)
        reiP = Peca("rei", "preto", Sprite("Sprites/reiP.png"), 0, 4)
        bispoP2 = Peca("bispo", "preto", Sprite("Sprites/bispoP.png"), 0, 5)
        cavaloP2 = Peca("cavalo", "preto", Sprite("Sprites/cavaloP.png"), 0, 6)
        torreP2 = Peca("torre", "preto", Sprite("Sprites/torreP.png"), 0, 7)
        peaoP1 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"),1,0)
        peaoP2 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 1)
        peaoP3 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 2)
        peaoP4 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 3)
        peaoP5 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 4)
        peaoP6 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 5)
        peaoP7 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 6)
        peaoP8 = Peca("peao", "preto", Sprite("Sprites/peaoP.png"), 1, 7)

        torreB1 = Peca("torre", "branco", Sprite("Sprites/torreB.png"),7,0)
        cavaloB1 = Peca("cavalo", "branco", Sprite("Sprites/cavaloB.png"),7,1)
        bispoB1 = Peca("bispo", "branco", Sprite("Sprites/bispoB.png"), 7, 2)
        rainhaB = Peca("rainha", "branco", Sprite("Sprites/rainhaB.png"), 7, 3)
        reiB = Peca("rei", "branco", Sprite("Sprites/reiB.png"), 7, 4)
        bispoB2 = Peca("bispo", "branco", Sprite("Sprites/bispoB.png"), 7, 5)
        cavaloB2 = Peca("cavalo", "branco", Sprite("Sprites/cavaloB.png"), 7, 6)
        torreB2 = Peca("torre", "branco", Sprite("Sprites/torreB.png"), 7, 7)
        peaoB1 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"),6,0)
        peaoB2 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 1)
        peaoB3 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 2)
        peaoB4 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 3)
        peaoB5 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 4)
        peaoB6 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 5)
        peaoB7 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 6)
        peaoB8 = Peca("peao", "branco", Sprite("Sprites/peaoB.png"), 6, 7)

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
                               self.mouse.is_over_object(self.matriz[i][j].sprite) and self.matriz[i][j].time=="branco"):
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
            if(self.selecao.tipo=="peao" and self.selecao.time=="branco"):
                disponivel = Peca("disponivel",None,Sprite("Sprites/verde.png"),self.selecao.linha-1,self.selecao.coluna)
                self.matriz[self.selecao.linha-1][self.selecao.coluna] = disponivel
                disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), self.selecao.linha -2,self.selecao.coluna)
                self.matriz[self.selecao.linha -2][self.selecao.coluna] = disponivel

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
