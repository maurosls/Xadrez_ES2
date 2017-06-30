

pretasComidas = []
brancasComidas = []
casaBrancosMortos = []
casaPretosMortos = []

     #Inicializaçao das casas dos mortos-------------------------------------------------------------------------------------------------------------------------------------------------
        cor = "preto"
     for i in range (0, 16):
           if (cor == "preto"):
                morto1 = Sprite("Sprites/morto-1.png")
                morto2 = Sprite("Sprites/morto-2.png")
                cor = "branco"
            else:
                morto1 = Sprite("Sprites/morto-2.png")
                morto2 = Sprite("Sprites/morto-1.png")
                cor = "preto"
            if( i < 8):
                morto1.x = 0
                morto2.x = 750
                index = i
            else:
                temp = morto1
                morto1 = morto2
                morto2 = temp
                morto1.x = 75
                morto2.x = 825
                index = i - 8
            morto1.y = index * self.tamanhoSprite
            morto2.y = index * self.tamanhoSprite
            self.casaBrancosMortos.append(morto1)
            self.casaPretosMortos.append(morto2)






    def moveOMorto(self, acao):
        if(self.matriz[acao.linha][acao.coluna].cor == "branco"):
            self.brancasComidas.append(self.matriz[acao.linha][acao.coluna])
            index = len(self.brancasComidas)-1      
            if(index < 8):
                self.matriz[acao.linha][acao.coluna].sprite.x = 0
            else:
                self.matriz[acao.linha][acao.coluna].sprite.x = 75
                index = index - 8
        if(self.matriz[acao.linha][acao.coluna].cor == "preto"):
            self.pretasComidas.append(self.matriz[acao.linha][acao.coluna])
            index = len(self.pretasComidas)-1
            if(index < 8):
                self.matriz[acao.linha][acao.coluna].sprite.x = 750
            else:
                self.matriz[acao.linha][acao.coluna].sprite.x = 825
                index = index - 8
        self.matriz[acao.linha][acao.coluna].sprite.y = 75 * index 

    def desenhaMat_de_Mortos(self):
        for i in range(0, len(self.casaBrancosMortos)):
            self.casaBrancosMortos[i].draw()
        for i in range(0, len(self.casaPretosMortos)):
            self.casaPretosMortos[i].draw()
        for i in range(0, len(self.brancasComidas)):
            self.brancasComidas[i].sprite.draw()
        for i in range(0, len(self.pretasComidas)):
            self.pretasComidas[i].sprite.draw()
