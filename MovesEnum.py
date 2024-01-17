from enum import Enum

class Move(Enum):
    COOPERATE = "\033[92m C\033[00m"
    DEFECT = "\033[91m D\033[00m"