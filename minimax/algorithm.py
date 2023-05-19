from copy import deepcopy

RED = (255,0,0)
Black = (255, 255, 255)

def minimax(position, depth, max_player):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, RED): #board, piece, move
            evaluation = minimax(move[0], depth-1, False)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, Black):
            evaluation = minimax(move[0], depth-1, True)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move


def alphabeta(position, depth, alpha, beta, max_player):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, RED):
            evaluation = alphabeta(move[0], depth-1, alpha, beta, False)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

            alpha = max(alpha, maxEval)
            if alpha >= beta:
                break
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, Black):
            evaluation = alphabeta(move[0], depth-1, alpha, beta, True)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

            beta = min(beta, minEval)
            if alpha >= beta:
                break

        return minEval, best_move


def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def get_all_moves(board, color):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append((new_board, (piece.row, piece.col), move))
    
    return moves