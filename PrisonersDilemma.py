from Player import Player
from MovesEnum import Move

class PrisonersDilemma:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    
    def evaluate_points(self, player1Move, player2Move):
        if player1Move==Move.COOPERATE and player2Move==Move.COOPERATE:
            self.player1.add_points(3)
            self.player2.add_points(3)
        elif player1Move==Move.DEFECT and player2Move==Move.COOPERATE:
            self.player1.add_points(5)
            self.player2.add_points(0)
        elif player1Move==Move.COOPERATE and player2Move==Move.DEFECT:
            self.player1.add_points(0)
            self.player2.add_points(5)
        elif player1Move==Move.DEFECT and player2Move==Move.DEFECT:
            self.player1.add_points(1)
            self.player2.add_points(1)

        self.player1.update_move_history(player1Move)
        self.player2.update_move_history(player2Move)

