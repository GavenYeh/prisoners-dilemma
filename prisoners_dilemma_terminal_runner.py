from Player import Player
from PrisonersDilemma import PrisonersDilemma
from MovesEnum import Move
import random

player1 = Player("1")
player2 = Player("2")

pd = PrisonersDilemma (player1, player2)

round = 1
while round<=20:
    print('\nRound {}'.format(round))
    while True:
        player1Move = int(input("Cooperate or defect? (1 for cooperate, 2 for defect) \n"))
        if player1Move in [1, 2]:
            break
        print("Invalid move, try again.")

    player2Move = random.choice([1,2])

    def mapInputToMove(moveInt):
        from MovesEnum import Move
        return Move.COOPERATE if moveInt==1 else Move.DEFECT

    player1Move = mapInputToMove(player1Move)
    player2Move = mapInputToMove(player2Move)

    pd.evaluate_points(player1Move, player2Move)

    print("player1 | {} | {}".format(''.join([move.value for move in player1.move_history]), player1.points))
    print("player2 | {} | {}".format(''.join([move.value for move in player2.move_history]), player2.points))
    print(15*'=')
    round+=1