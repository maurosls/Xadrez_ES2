class node:
    custoPai = None
    cost = -1
    tabuleiro = None
    linhaAntiga = None
    colunaAntiga = None
    linhaNova = None
    colunaNova = None
    pecaComida = None
    def __init__(self,cost,linhaAntiga,colunaAntiga,linhaNova,colunaNova):
        self.cost = cost
        self.linhaAntiga = linhaAntiga
        self.linhaNova = linhaNova
        self.colunaAntiga = colunaAntiga
        self.colunaNova = colunaNova