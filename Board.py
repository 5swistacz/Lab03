import random
import copy

class Board:
    def __init__(self):
        self.board = [None] + list(range(1, 10))
        self.winning_combos = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),
            (1, 5, 9),
            (3, 5, 7),
        ]

        self.corners = [0, 2, 6, 8]
        self.sides = [1, 3, 5, 7]
        self.middle = 4

    def print_board(self):
        print(self.board[7], self.board[8], self.board[9])
        print(self.board[4], self.board[5], self.board[6])
        print(self.board[1], self.board[2], self.board[3])
        print()

    def is_winner(self, marker):
        "check if this marker will win the game"
        # order of checks:
        #   1. across the horizontal top
        #   2. across the horizontal middle
        #   3. across the horizontal bottom
        #   4. across the vertical left
        #   5. across the vertical middle
        #   6. across the vertical right
        #   7. across first diagonal
        #   8. across second diagonal
        for combo in self.winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == marker:
                return True
        return False

    def get_bot_move(self, bot_marker):
        for i in range(1, len(self.board)):
            # board_copy = copy.deepcopy(self.board)
            if self.is_space_free(self.board, i):
                return i
                # self.make_move(i, bot_marker)
                # if self.is_winner(bot_marker):
                #     return i

    def is_space_free(self, board, index):
        "checks for free space of the board"
        return board[index] != 'X' and board[index] != 'O'

    def is_board_full(self):
        "checks if the board is full"
        for i in range(1, 9):
            if self.is_space_free(self.board, i):
                return False
        return True

    def make_move(self, index, move):
        self.board[index] = move

    def choose_random_move(self, move_list):
        possible_winning_moves = []
        for index in move_list:
            if self.is_space_free(self.board, index):
                possible_winning_moves.append(index)
                if len(possible_winning_moves) != 0:
                    return random.choice(possible_winning_moves)
                else:
                    return None

    def get_player_move(self):
        move = int(input("Pick a spot to move: (1-9) "))
        while move not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not self.is_space_free(self.board, move ):
            move = int(input("Invalid move. Please try again: (1-9) "))
        return move