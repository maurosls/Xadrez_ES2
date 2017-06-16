class Peca:
    tipo = None
    cor = None
    sprite = None
    linha = None
    coluna = None
    jaMoveu = False
    alvo = False
    spriteBackup = None
    value = None
    def __init__(self,tipo,time,sprite,linha,coluna,ja_moveu):
        self.tipo = tipo
        if(self.tipo == "peao"):
            self.value = 1
        elif(self.tipo == "torre"):
            self.value = 5
        elif(self.tipo == "bispo"):
            self.value = 3
        elif(self.tipo == "cavalo"):
            self.value = 3
        elif(self.tipo == "rainha"):
            self.value = 9
        elif(self.tipo == "rei"):
            self.value = 100
        else:
            self.value = 0
        self.cor = time
        self.sprite = sprite
        self.linha = linha
        self.coluna = coluna
        self.jaMoveu = ja_moveu
       # self.spriteBackup = sprite
        self.alvo = False
