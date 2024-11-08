# AI-Chess-Game-Player-vs-AI-

Overview: This is a simple text-based chess game where you can play against an AI opponent. The game follows traditional chess rules, and the AI uses a basic minimax algorithm with alpha-beta pruning to evaluate the best possible moves. You can play as either the white or black side, and the game provides turn-based interactions, with each player (you and the AI) making one move at a time.

Game Features:

Player vs AI:

You can play against an AI opponent, which uses a minimax algorithm to evaluate the best moves.
The AI simulates all possible moves up to a given depth and selects the optimal move based on material value.
Simplified Chess Rules:

All chess pieces (Pawn, Knight, Bishop, Rook, Queen, King) follow traditional movement rules.
Pieces are captured when moved to an occupied square by an opposing piece.
The game supports basic rules for "check" and "checkmate."
You can move pieces one square at a time (unless it's a special move like castling or en passant).
Material Evaluation:

The AI evaluates board positions based on the material balance (i.e., the number and value of pieces on the board).
Piece values are:
Pawn = 1 point
Knight = 3 points
Bishop = 3 points
Rook = 5 points
Queen = 9 points
King = 0 points (since capturing the King results in checkmate)
Turn-Based Gameplay:

Each player alternates turns: white goes first.
After every move, the game prints the updated board.
The game will automatically check for check conditions after each move.
Input Format:

Players input moves using standard chess notation (e.g., "a2 to a4" for moving a pawn).
The board is represented with columns labeled 'a' to 'h' and rows numbered 1 to 8.
Endgame Conditions:

The game ends when a player's King is checkmated (captured).
The game also ends in a stalemate if no legal moves remain for the player to make, and the King is not in check.
AI Behavior:

The AI calculates all possible moves at a certain depth (you can modify the depth for more or less challenging gameplay).
It uses the minimax algorithm to evaluate all possible game states and picks the move that maximizes its chances of winning while minimizing your advantage.
The AI opponent will make the best possible move based on the current board state.
Board Representation:

The chessboard is displayed in the terminal after every move.
Pieces are represented as abbreviations of their names (e.g., K for King, Q for Queen).
Empty squares are denoted with "--" for readability.
