class TicTacToe:
    def __init__(self):
        self.board = [" " for i in range(9)]

    def print_board(self):
        # for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
        #     print("| " +" | ".join(row)+" |")

        # for row in range(3):

        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_numbers():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

toe = TicTacToe()

toe.print_board_numbers()
