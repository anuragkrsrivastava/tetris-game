# tetris-game
Text Mode Tetris Game

To Start the Game, run game.py file. You can run game.py file using command "python game.py" 

There are 5 moves. a, d, w, s and space. For these moves, you need to input character a, d, w, s and " " (space character not the word space)

Convention :- 
top left tetris board point has coordinate (0, 1)
top right tetris board point is (13, 1)
bottom left tetris board point is (0, 13)
bottom right tetris board point is (13, 13), (Note:- pieces appears in between these points)

Anti clockwise or clockwise movement of pieces take place w.r.t piece point having minimum x-coordinate and y-coordinate

There are 4 files in this project:-

point.py - It has code about location of (2-D) points on tetris game and methods related to it

piece.py - It has code about 5 pieces that appears on tetris game board and methods related to it. 

move.py - It has code about 5 moves (a, d, w, s and " ") of pieces and methods related to it.

game.py - It combines the code of piece and move and form a game

(For more details comments are added in code)

(Note:- Unit tests are added for piece, move and game. To run Unit test, run command "pytest (name of file)")

(IMP Note:- If you are rotating piece in one direction, complete the full circle then rotate is other direction and vice-versa)
