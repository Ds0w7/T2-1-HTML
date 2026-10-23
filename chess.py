import chess
import random

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0
}

def evaluate(board):
    score = 0

    for piece_type in PIECE_VALUES:
        score += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]

    return score

def minimax(board, depth, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate(board), None

    best_move = None

    if maximizing:
        max_eval = -999999

        for move in board.legal_moves:
            board.push(move)
            eval_score, _ = minimax(board, depth - 1, False)
            board.pop()

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move

        return max_eval, best_move

    else:
        min_eval = 999999

        for move in board.legal_moves:
            board.push(move)
            eval_score, _ = minimax(board, depth - 1, True)
            board.pop()

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move

        return min_eval, best_move

board = chess.Board()

while not board.is_game_over():
    print(board)
    print()

    if board.turn == chess.WHITE:
        move = input("Tu jugada: ")
        board.push_san(move)
    else:
        _, best_move = minimax(board, 3, False)
        print("Bot juega:", best_move)
        board.push(best_move)

print("Fin de la partida")
