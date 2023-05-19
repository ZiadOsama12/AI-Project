from checkers.constants import RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax, alphabeta
from tmpboard import Board
import time
import tkinter as tk

# Global variables
game = Game()
tmpboard = Board()
difficulty_var = None
algorithm_var = None

def make_move():
    time.sleep(3)
    global game, tmpboard, difficulty_var, algorithm_var
    while(1):
        difficulty = int(difficulty_var.get())
        algorithm = int(algorithm_var.get())

        game_board, game_end = tmpboard.get_game_grid()
        tmpboard.print_grid(game_board)
        game.set_board(game_board)

        if algorithm == 1:
            value, new_board = minimax(game.get_board(), difficulty + 1, RED)
        else:
            value, new_board = alphabeta(game.get_board(), difficulty + 1, float('-inf'), float('inf'), RED)

        tmpboard.select_column(new_board[1][0], new_board[1][1])
        time.sleep(1)
        tmpboard.select_column(new_board[2][0], new_board[2][1])

        time.sleep(2)
        if game.winner() is not None:
            print(game.winner())

def main():
    global difficulty_var, algorithm_var

    root = tk.Tk()
    root.title("Checkers AI")
    root.configure(background="light gray")

    difficulty_label = tk.Label(root, text="Difficulty:", background="light gray")
    difficulty_label.pack()

    difficulty_var = tk.StringVar()
    difficulty_var.set("1")
    difficulty_radio_frame = tk.Frame(root, background="light gray")
    difficulty_radio_frame.pack()

    difficulty_radio_easy = tk.Radiobutton(difficulty_radio_frame, text="Easy", variable=difficulty_var, value="1", background="light gray")
    difficulty_radio_easy.pack(side=tk.LEFT)

    difficulty_radio_medium = tk.Radiobutton(difficulty_radio_frame, text="Medium", variable=difficulty_var, value="2", background="light gray")
    difficulty_radio_medium.pack(side=tk.LEFT)

    difficulty_radio_hard = tk.Radiobutton(difficulty_radio_frame, text="Hard", variable=difficulty_var, value="3", background="light gray")
    difficulty_radio_hard.pack(side=tk.LEFT)

    algorithm_label = tk.Label(root, text="Algorithm:", background="light gray")
    algorithm_label.pack()

    algorithm_var = tk.StringVar()
    algorithm_var.set("1")
    algorithm_radio_frame = tk.Frame(root, background="light gray")
    algorithm_radio_frame.pack()

    algorithm_radio_minimax = tk.Radiobutton(algorithm_radio_frame, text="Minimax", variable=algorithm_var, value="1", background="light gray")
    algorithm_radio_minimax.pack(side=tk.LEFT)

    algorithm_radio_alphabeta = tk.Radiobutton(algorithm_radio_frame, text="Alphabeta", variable=algorithm_var, value="2", background="light gray")
    algorithm_radio_alphabeta.pack(side=tk.LEFT)

    move_button = tk.Button(root, text="Make Move", command=make_move, background="gray")
    move_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
