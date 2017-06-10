class Peca:
    tipo = None
    cor = None
    sprite = None
    linha = None
    coluna = None
    jaMoveu = False
    alvo = False
    spriteBackup = None
    def __init__(self,tipo,time,sprite,linha,coluna,ja_moveu):
        self.tipo = tipo
        self.cor = time
        self.sprite = sprite
        self.linha = linha
        self.coluna = coluna
        self.jaMoveu = ja_moveu
       # self.spriteBackup = sprite
        self.alvo = False
