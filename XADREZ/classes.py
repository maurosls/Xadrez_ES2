class Table:
    sides = []
    table = [[],[]]

class Side:
    chessmans = []
    isInCheck = False
    isAiControlled = False
    difficulty = 0

class Movement:
    position = [[],[]] #TODO: TROCAR PARA ARRAY COM 2 POSIÇÕES (X,Y)
    cost = 0

class Chessman:
    position = [[],[]] #TODO: TROCAR PARA ARRAY COM 2 POSIÇÕES (X,Y)
    nextMoves = [[],Movement] #TODO: ARRAY DE UMA DIMENSÃO COM OS OBJ MOVEMENT
    cost = 0
    name = "empty"
    def move(newPosition):
        position = newPosition
    def calculateNextMoves(self):
        return

class King(Chessman):
    def calculateNextMoves(self):
        return
class Queen(Chessman):
    def calculateNextMoves(self):
        return
class Rook(Chessman):
    def calculateNextMoves(self):
        return
class Bishop(Chessman):
    def calculateNextMoves(self):
        return
class Knight(Chessman):
    def calculateNextMoves(self):
        return
class Pawn(Chessman):
    def calculateNextMoves(self):
        return



