class Peca:
    tipo = None
    time = None
    sprite = None
    linha = None
    coluna = None
    ja_moveu = False
    alvo = False
    spriteBackup = None
    def __init__(self,tipo,time,sprite,linha,coluna,ja_moveu):
        self.tipo = tipo
        self.time = time
        self.sprite = sprite
        self.linha = linha
        self.coluna = coluna
        self.ja_moveu = ja_moveu
        self.spriteBackup = sprite
        self.alvo = False
