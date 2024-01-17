class Player:

    def __init__(self, player_number):
        self.player_number = player_number
        self.points = 0
        self.move_history = []

    def add_points(self, points):
        self.points+=points
        print("player {} gained {} points".format(self.player_number, points))
        # print("player {} now has {} points".format(
        #     self.player_number, self.points))

    def update_move_history(self, move):
        self.move_history.append(move)


