# Artificial-Intelligence



Implementation of Game Theory with Adversarial Search

Rules:
Each player has 16  pieces to start the game: one king, one queen, two rooks, two bishops, two knights and eight pawns. 
The object of the game is to capture the other player's king. This capture is never actually completed, but once a king is under attack and unable to avoid capture, it is said to be checkmated and the game is over. 
A move consists of placing one piece on a different square, following the rules of movement for that piece.  A player can take an opponent's piece by moving one of his or her own pieces to the square that contains an opponent's piece. The opponent's piece is removed from the board and is out of play for the rest of the game. 
Check If a King is threatened with capture, but has a means to escape, then it is said to be in check. A King cannot move into check, and if in check must move out of check immediately. There are three ways you may move out of check:
	1. Capture the checking piece
	2. Block the line of attack by placing one of your own pieces between the 	    checking piece and the King. (Of course, a Knight cannot be blocked.) 
	3. Move the King away from check. 
Checkmate The primary objective in chess is to checkmate your opponent's King. When a King cannot avoid capture then it is checkmated and the game is immediately over. 
Stalemate The game is drawn when the player to move has no legal move and his king is not in check. The game is said to end in 'stalemate'. This immediately ends the game. 


![screen shot 2018-06-21 at 11 57 40 am](https://user-images.githubusercontent.com/28520902/41730808-b5366dca-754a-11e8-814b-89974a3bc5b1.png)

![screen shot 2018-06-21 at 12 01 43 pm](https://user-images.githubusercontent.com/28520902/41730919-079f1d0a-754b-11e8-8d7e-70f6bfd34615.png)

Search-Tree using Alpha beta Pruning Algorithm with Minimax

Alpha = best already explored option along path to the root for maximizer
Beta = best already explored option  along path to the root for minimizer
Alpha-beta pruning is an optimization method to the minimax algorithm that allows us to disregard some branches in the search tree. 
The alpha-beta pruning is based on the situation where we can stop evaluating a part of the search tree if we find a move that leads to a worse situation than a previously discovered move.

The alpha-beta pruning does not influence the outcome of the minimax algorithm — it only makes it faster.

The alpha-beta algorithm also is more efficient if we happen to visit first those paths that lead to good moves.

![screen shot 2018-06-21 at 12 02 03 pm](https://user-images.githubusercontent.com/28520902/41730921-08ffae12-754b-11e8-837e-6ac47fb29262.png)

With alpha-beta, we get a significant boost to the minimax algorithm, as is shown in the following example:

![screen shot 2018-06-21 at 12 02 08 pm](https://user-images.githubusercontent.com/28520902/41730925-0a5f1158-754b-11e8-94ae-9da3dab34d32.png)
The number of positions that are required
 to evaluate if we want to perform a search
 with depth of 4 and the “root” position
 is the one that is shown.
