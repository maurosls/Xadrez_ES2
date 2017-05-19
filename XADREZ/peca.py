class Peca:
    tipo = None
    time = None
    sprite = None
    linha = None
    coluna = None

    def __init__(self,tipo,time,sprite,linha,coluna):
        self.tipo = tipo
        self.time = time
        self.sprite = sprite
        self.linha = linha
        self.coluna = coluna
