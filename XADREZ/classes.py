class Table:
    sides = []
    table = [[],[]]

class Side:
    chessmans = []
    isInCheck = False
    isAiControlled = False
    difficulty = 0

class Movement:
    position = [[],[]]
    cost = 0

class Chessman:
    position = [[],[]]
    nextMoves = [[],Movement]
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



