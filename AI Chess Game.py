import random
import time

# Define constants for piece values
PIECE_VALUES = {
    'pawn': 1,
    'knight': 3,
    'bishop': 3,
    'rook': 5,
    'queen': 9,
    'king': 0  # King doesn't have a value in terms of material, as losing it ends the game
}

class ChessPiece:
    """Represents a chess piece on the board."""
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"{self.color[0].upper()}{self.name[0].upper()}"


class ChessBoard:
    """Represents a chessboard and manages the game state."""
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        """Set up the initial positions of pieces on the board."""
        # White pieces
        self.board[0] = [ChessPiece('white', 'rook'), ChessPiece('white', 'knight'), ChessPiece('white', 'bishop'),
                         ChessPiece('white', 'queen'), ChessPiece('white', 'king'), ChessPiece('white', 'bishop'),
                         ChessPiece('white', 'knight'), ChessPiece('white', 'rook')]
        self.board[1] = [ChessPiece('white', 'pawn')] * 8

        # Black pieces
        self.board[7] = [ChessPiece('black', 'rook'), ChessPiece('black', 'knight'), ChessPiece('black', 'bishop'),
                         ChessPiece('black', 'queen'), ChessPiece('black', 'king'), ChessPiece('black', 'bishop'),
                         ChessPiece('black', 'knight'), ChessPiece('black', 'rook')]
        self.board[6] = [ChessPiece('black', 'pawn')] * 8

    def print_board(self):
        """Print the current state of the board."""
        for row in self.board:
            print(" ".join([str(piece) if piece else '--' for piece in row]))

    def move_piece(self, start, end, color):
        """Move a piece from start to end position."""
        start_row, start_col = start
        end_row, end_col = end

        piece = self.board[start_row][start_col]
        if piece is None:
            print("No piece at the starting position!")
            return False
        if piece.color != color:
            print(f"Not your turn! You are {color} and the piece is {piece.color}.")
            return False
        if not self.is_valid_move(piece, start, end):
            print("Invalid move!")
            return False

        # Make the move
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = None
        return True

    def is_valid_move(self, piece, start, end):
        """Check if a move is valid for a given piece (simplified logic)."""
        start_row, start_col = start
        end_row, end_col = end

        if piece.name == 'pawn':
            direction = 1 if piece.color == 'white' else -1
            if start_col == end_col and self.board[end_row][end_col] is None:  # Moving forward
                if abs(end_row - start_row) == 1:
                    return True
                if abs(end_row - start_row) == 2 and (start_row == 1 or start_row == 6):
                    return True
            elif abs(end_col - start_col) == 1 and end_row - start_row == direction:
                if self.board[end_row][end_col] and self.board[end_row][end_col].color != piece.color:
                    return True

        elif piece.name == 'rook':
            if start_row == end_row or start_col == end_col:
                return True

        elif piece.name == 'knight':
            if abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1:
                return True
            if abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2:
                return True

        elif piece.name == 'bishop':
            if abs(start_row - end_row) == abs(start_col - end_col):
                return True

        elif piece.name == 'queen':
            if abs(start_row - end_row) == abs(start_col - end_col) or start_row == end_row or start_col == end_col:
                return True

        elif piece.name == 'king':
            if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
                return True

        return False

    def is_check(self, color):
        """Check if the king of a given color is under attack."""
        king_position = None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.name == 'king' and piece.color == color:
                    king_position = (row, col)
                    break

        if not king_position:
            return False

        opponent_color = 'black' if color == 'white' else 'white'
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == opponent_color:
                    if self.is_valid_move(piece, (row, col), king_position):
                        return True

        return False

    def evaluate_board(self):
        """Evaluate the board's score based on material value."""
        score = 0
        for row in self.board:
            for piece in row:
                if piece:
                    piece_value = PIECE_VALUES.get(piece.name, 0)
                    if piece.color == 'white':
                        score += piece_value
                    else:
                        score -= piece_value
        return score


def minimax(board, depth, is_maximizing_player, alpha, beta, color):
    """Minimax algorithm with alpha-beta pruning to evaluate the best move."""
    if depth == 0:
        return board.evaluate_board()

    possible_moves = get_possible_moves(board, color)
    if is_maximizing_player:
        max_eval = float('-inf')
        for move in possible_moves:
            new_board = board.clone()
            new_board.move_piece(move[0], move[1], color)
            eval = minimax(new_board, depth - 1, False, alpha, beta, 'black' if color == 'white' else 'white')
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in possible_moves:
            new_board = board.clone()
            new_board.move_piece(move[0], move[1], color)
            eval = minimax(new_board, depth - 1, True, alpha, beta, 'black' if color == 'white' else 'white')
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def get_possible_moves(board, color):
    """Generate all possible moves for a given color."""
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board.board[row][col]
            if piece and piece.color == color:
                for i in range(8):
                    for j in range(8):
                        if (row != i or col != j) and board.is_valid_move(piece, (row, col), (i, j)):
                            moves.append(((row, col), (i, j)))
    return moves


def main():
    chess_board = ChessBoard()
    current_turn = 'white'
    game_over = False

    while not game_over:
        chess_board.print_board()
        if current_turn == 'white':
            start = input("Enter the starting position (e.g. 'a2'): ").strip().lower()
            end = input("Enter the ending position (e.g. 'a4'): ").strip().lower()

            start_row = 8 - int(start[1])
            start_col = ord(start[0]) - ord('a')
            end_row = 8 - int(end[1])
print(main())