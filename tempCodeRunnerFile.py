# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
#import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax
from tmpboard import Board
import time
import tkinter as tk


#WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col



def main():
    run = True
    #clock = pygame.time.Clock()
    game = Game()

    while 1:
        #clock.tick(FPS)
        tmpboard = Board()
        (game_board, game_end) = tmpboard.get_game_grid()
        tmpboard.print_grid(game_board)
        #break
        game.set_board(game_board)
        print("red kings \n") 
        print(game.get_board().red_kings)

        print("white kings \n") 
        print(game.get_board().white_kings)

        difficulty = 1
        #if game.turn == WHITE:
        value, new_board = minimax(game.get_board(), difficulty + 1, RED)
        #game.ai_move(new_board[0])
        
        #print("Piece: ")
        #print(new_board[1])
        #print('\n')
        #print("TO: ")
        #print(new_board[2])
        #print('\n')

        #break
        tmpboard.select_column((new_board[1][0]), new_board[1][1])
        time.sleep(1)
        tmpboard.select_column((new_board[2][0]), new_board[2][1])

        time.sleep(3)
        if game.winner() != None:
            print(game.winner())
            run = False

        #for event in pygame.event.get():
         #   if event.type == pygame.QUIT:
          #      run = False
            
           # if event.type == pygame.MOUSEBUTTONDOWN:
            #    pos = pygame.mouse.get_pos()
             #   row, col = get_row_col_from_mouse(pos)
            #game.select(row, col) #MODIFYYYYYYYY

        #game.update()
    
    #pygame.quit()

main()