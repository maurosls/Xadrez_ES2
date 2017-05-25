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

    pretasComidas = []
    brancasComidas = []
    casas = None
    selecao = None

    rodada = None

    matriz = None


    def __init__(self):
        self.janela = Window(1100, 600)
        self.mouse = self.janela.get_mouse()

        pygame.display.set_caption("Trabalho ---- ES2") # Coloca titulo no trabalho

# interface grafica do jogo referente ao tempo e troca de turno -----------------------------------------------------------------------

        self.spritevez = Sprite("Sprites/vezdo.png")
        self.spritevez.x = 670
        self.spritevez.y = 250

        self.ppreta = Sprite("Sprites/ppreta.png")
        self.ppreta.x = 800
        self.ppreta.y = 330

        self.pbranca = Sprite("Sprites/pbranco.png")
        self.pbranca.x = 800
        self.pbranca.y = 380

        self.apontaj = Sprite("Sprites/apontaj.png")
        self.apontaj.x = 730
        self.apontaj.y = 380

        self.tempoj = Sprite("Sprites/tempoj.png")
        self.tempoj.x = 670
        self.tempoj.y = 450

        self.tempot = Sprite("Sprites/tempot.png")
        self.tempot.x = 670
        self.tempot.y = 530

        self.tempoIni = pygame.time.get_ticks()
        self.tempoInij = pygame.time.get_ticks()

        self.efeito3d = Sprite("Sprites/efeito3d.png")
        self.efeito3d.x = 600
        self.efeito3d.y = 0
#-------------------------------------------------------------------------------------------------------------------------------------------------
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
        self.rodada = "branco"
        self.selecaoSprite = Sprite("Sprites/selecao.png")
        self.selecaoSprite.x = self.janela.width
        self.selecaoSprite.y = self.janela.height

# método para verificar o tempo do jogo ---------------------------------------------------------------------------------------------------------

    def timerG(self, start, end):
        self.hours, self.rem = divmod(end/1000 - start/1000,3600)
        self.minutes, self.seconds = divmod(self.rem, 60)
        self.stringResp = "{:0>2}:{:0>2}:{:05.2f}".format(int(self.hours), int(self.minutes), self.seconds)
        self.janela.draw_text(self.stringResp, 900, self.tempot.y, 30, (8, 8, 8))

# metodo para verificar o tempo de 1 jogada ------------------------------------------------------------------------------------------------------------------
    def timerJ(self, start, end):
        self.hours, self.rem = divmod(end/1000 - start/1000, 3600)
        self.minutes, self.seconds = divmod(self.rem, 60)
        self.stringResp = "{:0>2}:{:0>2}:{:05.2f}".format(int(self.hours), int(self.minutes), self.seconds)
        self.janela.draw_text(self.stringResp, 900, self.tempoj.y, 30, (8, 8, 8))

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
                                    elif(self.matriz[x][y].alvo == True):
                                        self.matriz[x][y].alvo = False
                                        self.matriz[x][y].sprite = self.matriz[x][y].spriteBackup
                        self.janela.update()
                        self.selecaoSprite.x = self.matriz[i][j].sprite.x
                        self.selecaoSprite.y = self.matriz[i][j].sprite.y
                        self.selecao = self.matriz[i][j]

#----Função que implementa a movimentação do bispo.
#----Se assemelha com a implementação do rei e do cavalo.
#----No if, os argumentos são as direções de verificação.
    def movimento_bispo(self, inc_linha = 0, inc_coluna = 0):
        if(inc_linha == 0 and inc_coluna == 0):
            self.movimento_bispo( 1,  1)
            self.movimento_bispo( 1, -1)
            self.movimento_bispo(-1,  1)
            self.movimento_bispo(-1, -1)
        else:
            i = self.selecao.linha + inc_linha
            j = self.selecao.coluna + inc_coluna
            while(i >= 0 and                                
                  i < len(self.matriz) and                  
                  j >= 0 and                                # condição que verifica se as posições i e j 
                  j < len(self.matriz[0])):                 # continuam dentro do tabuleiro
               
                if(self.matriz[i][j] == "vazio"):
                    disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), i,
                                              j, False)
                    self.matriz[i][j] = disponivel
                    i = i + inc_linha
                    j = j + inc_coluna
                else:
                    break


    def movimento_peao(self):
        # ---------------------------------> a partir daqui peoes brancos -------------------------------------------------------------------------------
        if(self.selecao.time=="branco"):
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
        if (self.selecao.time == "preto"):
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

#----Função que implementa a movimentação da torre.
#----Cada "for" resolve uma direção calculando os limites.
#----Caso encontre uma peça ou esteja no fim do tabuleiro ele sai do loop.
    def movimento_torre(self):
        #---for decremental: calcula todas as posições a cima da torre 
        for i in range (self.selecao.linha-1, -1, -1):
            if(self.matriz[i][self.selecao.coluna] == "vazio"):
                disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), i,
                                          self.selecao.coluna, False)
                self.matriz[i][self.selecao.coluna] = disponivel
            else:
                break
        #---for incremental: calcula todas as posições a direita da torre
        for i in range(self.selecao.coluna+1, len(self.matriz[0])):
            if(self.matriz[self.selecao.linha][i] == "vazio"):
                disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), self.selecao.linha,
                                      i, False)
                self.matriz[self.selecao.linha][i] = disponivel
            else:
                break  
        #---for incremental: calcula todas as posições a baixo da torre
        for i in range (self.selecao.linha+1, len(self.matriz)):
            if(self.matriz[i][self.selecao.coluna] == "vazio"):
                disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), i,
                                         self.selecao.coluna, False)
                self.matriz[i][self.selecao.coluna] = disponivel
            else:
                break
        #---for decremental: calcula todas as posições a esquerda da torre
        for i in range(self.selecao.coluna-1, -1, -1):
            if(self.matriz[self.selecao.linha][i] == "vazio"):
                disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), self.selecao.linha,
                                              i, False)
                self.matriz[self.selecao.linha][i] = disponivel
            else:
                break 

#----Função que implementa a movimentação do rei
#----de uma forma que se parece com uma recursão.
#----Caso os parâmetros sejam 0, ele inicia o calculo
#----para todas as possibilidades de movimentos do rei,
#----fiz isso para evitar repetição de "if's".
    def movimento_rei(self, linha, coluna):
        if(linha == self.selecao.linha and coluna == self.selecao.coluna):
            self.movimento_rei(linha, coluna + 1)
            self.movimento_rei(linha, coluna - 1)
            self.movimento_rei(linha + 1, coluna)
            self.movimento_rei(linha + 1, coluna + 1)
            self.movimento_rei(linha + 1, coluna - 1)
            self.movimento_rei(linha - 1, coluna)
            self.movimento_rei(linha - 1, coluna + 1)
            self.movimento_rei(linha - 1, coluna - 1)
        else:
            if(linha >= 0 and linha < len(self.matriz) and coluna >=0 and coluna < len(self.matriz[0])):
                if(self.matriz[linha][coluna] == "vazio"):
                    disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), linha,
                                                  coluna, False)
                    self.matriz[linha][coluna] = disponivel

#----Função que implementa a movimentação do cavalo.
#----Se assemelha com a implementação da movimentação do rei.
    def movimento_cavalo(self, inc_linha = 0, inc_coluna = 0):
        if(inc_linha == 0 and inc_coluna == 0):
            self.movimento_cavalo( 1,  2)
            self.movimento_cavalo( 1, -2)
            self.movimento_cavalo(-1,  2)
            self.movimento_cavalo(-1, -2)
            self.movimento_cavalo( 2,  1)
            self.movimento_cavalo( 2, -1)
            self.movimento_cavalo(-2,  1)
            self.movimento_cavalo(-2, -1)
        else:
            i = self.selecao.linha + inc_linha
            j = self.selecao.coluna + inc_coluna
            if(i >= 0 and
               i < len(self.matriz) and
               j >= 0 and
               j < len(self.matriz[0])):
                if(self.matriz[i][j] == "vazio"):
                    disponivel = Peca("disponivel", None, Sprite("Sprites/verde.png"), i,
                                                  j, False)
                    self.matriz[i][j] = disponivel


    def defineDisponiveis(self):
        if (self.selecao!=None and self.selecao.time == self.rodada):

            if(self.selecao.tipo == "peao"):
                self.movimento_peao()
            if(self.selecao.tipo == "torre"):
                self.movimento_torre()

            if(self.selecao.tipo == "bispo"):
                self.movimento_bispo()

            if(self.selecao.tipo == "rei"):
                self.movimento_rei(self.selecao.linha, self.selecao.coluna)

            if(self.selecao.tipo == "rainha"):
                self.movimento_bispo()
                self.movimento_torre()

            if(self.selecao.tipo == "cavalo"):
                self.movimento_cavalo()

    def defineAlvos(self):
        if(self.selecao != None):
            if(self.selecao.time == self.rodada):
                if(self.selecao.tipo == "peao"):
                    if(self.rodada == "branco"):
                        lin = self.selecao.linha - 1;
                        colD = self.selecao.coluna + 1;
                        colE = self.selecao.coluna - 1;
                    if(self.rodada == "preto"):
                        lin = self.selecao.linha + 1;
                        colD = self.selecao.coluna + 1;
                        colE = self.selecao.coluna - 1;
                    if(lin >= 0  and lin < len(self.matriz[0])):
                        if(colD < len(self.matriz[0])):
                            if(self.matriz[lin][colD] != "vazio"):
                                if(self.matriz[lin][colD].time != self.rodada):
                                    self.matriz[lin][colD].alvo = True
                        if(colE > 0):
                            if(self.matriz[lin][colE] != "vazio"):
                                if(self.matriz[lin][colE].time != self.rodada):
                                    self.matriz[lin][colE].alvo = True
                if(self.selecao.tipo == "torre"):
                    True

                if(self.selecao.tipo == "bispo"):
                    True
                if(self.selecao.tipo == "rei"):
                    True

                if(self.selecao.tipo == "rainha"):
                    True

                if(self.selecao.tipo == "cavalo"):
                    True


    def confirmaMovimento(self):
        updateMov = False
        updateAlvo = False
        acao = None
        for i in range(0,len(self.matriz)):
            for j in range(0, len(self.matriz[0])):
                if (self.matriz[i][j]!="vazio"):
                    while ((self.mouse.is_button_pressed(1) and self.mouse.is_over_object(self.matriz[i][j].sprite) and self.matriz[i][j].tipo=="disponivel")
                           or (self.mouse.is_button_pressed(1) and self.mouse.is_over_object(self.matriz[i][j].sprite) and self.matriz[i][j].alvo == True)):
                        self.janela.update()
                        if(self.matriz[i][j].tipo=="disponivel"):
                            updateMov = True

                        elif(self.matriz[i][j].alvo == True):
                            updateAlvo = True

                        acao = self.matriz[i][j]

        if (updateMov==True or updateAlvo==True):
            if(updateMov==True):
                self.matriz[self.selecao.linha][self.selecao.coluna] = "vazio"
                self.selecao.linha = acao.linha
                self.selecao.coluna = acao.coluna
                self.matriz[acao.linha][acao.coluna] = self.selecao
                if (self.selecao.tipo=="peao"):
                    self.selecao.ja_moveu = True

            elif(updateAlvo==True):
                if(self.matriz[acao.linha][acao.coluna].time == "branco"):
                    self.brancasComidas.append(self.matriz[acao.linha][acao.coluna])
                if(self.matriz[acao.linha][acao.coluna].time == "preto"):
                    self.pretasComidas.append(self.matriz[acao.linha][acao.coluna])
                self.matriz[self.selecao.linha][self.selecao.coluna] = "vazio"
                self.selecao.linha = acao.linha
                self.selecao.coluna = acao.coluna
                self.matriz[acao.linha][acao.coluna] = self.selecao

            if(self.rodada == "branco"):
                self.rodada = "preto"
                # toda vez que troca a jogada o tempo zera e a seta muda
                self.apontaj.y = self.ppreta.y
                self.tempoInij = pygame.time.get_ticks()
            else:
                self.rodada = "branco"
                # toda vez que troca a jogada o tempo zera e a seta muda
                self.apontaj.y = self.pbranca.y
                self.tempoInij = pygame.time.get_ticks()
            self.selecao = None
            self.selecaoSprite.x=self.janela.width
            self.selecaoSprite.y=self.janela.height

            for x in range(0, len(self.matriz)):
                for y in range(0, len(self.matriz[0])):
                    if (self.matriz[x][y] != "vazio"):
                        if (self.matriz[x][y].tipo == "disponivel"):
                            self.matriz[x][y] = "vazio"
                        elif(self.matriz[x][y].alvo == True):
                            self.matriz[x][y].alvo = False
                            self.matriz[x][y].sprite = self.matriz[x][y].spriteBackup


    def atualiza(self):
        self.janela.set_background_color(16777215)
        for i in range(0, len(self.casas)):
            self.casas[i].draw()

        for i in range(0,len(self.matriz)):
            for j in range(0,len(self.matriz[0])):
                if (self.matriz[i][j]!= "vazio"):
                    if(self.matriz[i][j].alvo == True):
                        self.matriz[i][j].sprite = Sprite("Sprites/vermelho.png")

                    self.matriz[i][j].sprite.x = j * self.tamanhoSprite
                    self.matriz[i][j].sprite.y = i * self.tamanhoSprite
                    self.matriz[i][j].sprite.draw()

        self.efeito3d.draw()
        self.spritevez.draw()
        self.ppreta.draw()
        self.pbranca.draw()
        self.apontaj.draw()
        self.tempoj.draw()
        self.tempot.draw()
        self.timerG(self.tempoIni, pygame.time.get_ticks())
        self.timerJ(self.tempoInij, pygame.time.get_ticks())
        self.selecaoSprite.draw()

        self.janela.update()
