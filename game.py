from piece import Piece, PieceType
from move import Move, MoveType
from point import Point
from random import randint


class Game:
    def __init__(self, board_right_up, board_right_down):
        self._game_piece = None
        self._game_move = None
        self._board_left_up = Point(1, 1)
        self._board_left_down = Point(1, board_right_down)
        self._board_right_up = Point(board_right_up, 1)
        self._board_right_down = Point(board_right_up, board_right_down)

    # update position of second piece which randomly positioned along x-axis
    @staticmethod
    def update_new_position(piece, new_position):
        point_1 = piece.point_1
        point_2 = piece.point_2
        point_3 = piece.point_3
        point_4 = piece.point_4
        new_point_2_position = point_2.x - point_1.x
        new_point_2_position = new_point_2_position + new_position
        piece.update_point_2(Point(new_point_2_position, point_2.y))
        new_point_3_position = point_3.x - point_1.x
        new_point_3_position = new_point_3_position + new_position
        piece.update_point_3(Point(new_point_3_position, point_3.y))
        new_point_4_position = point_4.x - point_1.x
        new_point_4_position = new_point_4_position + new_position
        piece.update_point_4(Point(new_point_4_position, point_4.y))
        piece.update_point_1(Point(new_position, point_1.y))
        return piece

    # setting position of piece on game board
    def set_game_piece(self, piece_type, horizontal_location=None):
        piece = Piece(PieceType[piece_type])
        if horizontal_location:
            self._game_piece = self.update_new_position(piece, horizontal_location)
        else:
            self._game_piece = piece

    def get_game_piece(self):
        return self._game_piece

    def set_game_piece_move(self, game_piece):
        self._game_move = Move(game_piece, self._board_left_up, self._board_left_down, self._board_right_up, self._board_right_down)

    # game play starts using start play method
    def start_play(self, move_type):
        if self._game_move.move_piece(move_type):
            piece = self._game_move.get_piece()
            piece_state = set()
            piece_state.add(piece.point_1)
            piece_state.add(piece.point_2)
            piece_state.add(piece.point_3)
            piece_state.add(piece.point_4)
            for vertical in range(self._board_left_up.y, self._board_left_down.y+1):
                print('*', end="")
                for horizontal in range(self._board_left_up.x, self._board_right_up.x+1):
                    flag = 0
                    for piece_point in piece_state:
                        if (piece_point.x == horizontal) and (piece_point.y == vertical):
                            print('*', end="")
                            flag = 1
                            break
                    if flag == 0:
                        print(' ', end="")
                print('*')
            for horizontal in range(self._board_left_up.x-1, self._board_right_up.x+2):
                print('*', end="")
            print()

    # game play ends by checking condition
    def end_play(self):
        piece = self._game_move.get_piece()
        if piece.point_1.y == self._board_left_down.y:
            return True
        if piece.point_2.y == self._board_left_down.y:
            return True
        if piece.point_3.y == self._board_left_down.y:
            return True
        if piece.point_4.y == self._board_left_down.y:
            return True
        return False


# Unit test cases for updating new position of randomly positioned second piece
def test_update_new_position():
    test_game = Game(12, 12)
    test_piece = test_game.update_new_position(Piece(PieceType.piece_1), 7)
    assert test_piece.point_1.x == 7
    assert test_piece.point_1.y == 1
    assert test_piece.point_2.x == 8
    assert test_piece.point_3.x == 9
    assert test_piece.point_4.x == 10


if __name__ == "__main__":
    game = Game(12, 12)
    random_piece_type = randint(1, 5)
    print('Piece number %d is randomly Selected ... for this Game ........\n' % random_piece_type)
    piece_type_input = 'piece_' + str(random_piece_type)
    game.set_game_piece(piece_type_input)
    first_piece = game.get_game_piece()
    game.set_game_piece_move(first_piece)
    while(True):
        print('Please input a move type a, d, w, s or space')
        move_type_input = input()
        if move_type_input == " ":
            move_type_input = 'move_space'
        else:
            move_type_input = 'move_' + move_type_input
        try:
            game.start_play(MoveType[move_type_input])
        except:
            print("Please Select a valid move between a, d, w, s or space ... Don't Select any other move......\n")
        if game.end_play():
            break
    print('Game is over for first piece ..............\n')
    print('Now Second piece is going to onboard Game .....\n')
    random_horizontal_position = randint(1, 9)
    game.set_game_piece(piece_type_input, random_horizontal_position)
    print('Second piece is positioned at position %d randomly along the x-axis ........\n' % random_horizontal_position)
    second_piece = game.get_game_piece()
    game.set_game_piece_move(second_piece)
    while (True):
        print('Please input a move type a, d, w, s or space')
        move_type_input = input()
        if move_type_input == " ":
            move_type_input = 'move_space'
        else:
            move_type_input = 'move_' + move_type_input
        try:
            game.start_play(MoveType[move_type_input])
        except:
            print("Please Select a valid move between a, d, w, s or space ... Don't Select any other move......\n")
        if game.end_play():
            break
    print('Game Ends !!! ......')
