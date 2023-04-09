from enum import Enum
from point import Point
from piece import Piece, PieceType


class MoveType(Enum):
    move_a = {'all': Point(-1, 1)}
    move_d = {'all': Point(1, 1)}
    move_w = {'piece_1': {1: {'point_2': Point(-1, -1), 'point_3': Point(-2, -2), 'point_4': Point(-3, -3)},
                          2: {'point_2': Point(-1, 1), 'point_3': Point(-2, 2), 'point_4': Point(-3, 3)},
                          3: {'point_2': Point(1, 1), 'point_3': Point(2, 2), 'point_4': Point(3, 3)},
                          0: {'point_2': Point(1, -1), 'point_3': Point(2, -2), 'point_4': Point(3, -3)}},
              'piece_2': {1: {'point_2': Point(1, -1), 'point_3': Point(2, -2), 'point_4': Point(1, -3)},
                          2: {'point_2': Point(-1, -1), 'point_3': Point(-2, -2), 'point_4': Point(-3, -1)},
                          3: {'point_2': Point(-1, 1), 'point_3': Point(-2, 2), 'point_4': Point(-1, 3)},
                          0: {'point_2': Point(1, 1), 'point_3': Point(2, 2), 'point_4': Point(3, 1)}},
              'piece_3': {1: {'point_2': Point(-3, 1), 'point_3': Point(-2, 0), 'point_4': Point(-1, -1)},
                          2: {'point_2': Point(1, 3), 'point_3': Point(0, 2), 'point_4': Point(-1, 1)},
                          3: {'point_2': Point(3, -1), 'point_3': Point(2, 0), 'point_4': Point(1, 1)},
                          0: {'point_2': Point(-1, -3), 'point_3': Point(0, -2), 'point_4': Point(1, -1)}},
              'piece_4': {1: {'point_2': Point(1, -1), 'point_3': Point(-2, 0), 'point_4': Point(-1, -1)},
                          2: {'point_2': Point(-1, -1), 'point_3': Point(0, 2), 'point_4': Point(-1, 1)},
                          3: {'point_2': Point(-1, 1), 'point_3': Point(2, 0), 'point_4': Point(1, 1)},
                          0: {'point_2': Point(1, 1), 'point_3': Point(0, -2), 'point_4': Point(1, -1)}},
              'piece_5': {1: {'point_2': Point(1, -1), 'point_3': Point(-1, -1), 'point_4': Point(0, -2)},
                          2: {'point_2': Point(-1, -1), 'point_3': Point(-1, 1), 'point_4': Point(-2, 0)},
                          3: {'point_2': Point(-1, 1), 'point_3': Point(1, 1), 'point_4': Point(0, 2)},
                          0: {'point_2': Point(1, 1), 'point_3': Point(1, -1), 'point_4': Point(2, 0)}}}
    move_s = {'piece_1': {1: {'point_2': Point(-1, 1), 'point_3': Point(-2, 2), 'point_4': Point(-3, 3)},
                          2: {'point_2': Point(-1, -1), 'point_3': Point(-2, -2), 'point_4': Point(-3, -3)},
                          3: {'point_2': Point(1, -1), 'point_3': Point(2, -2), 'point_4': Point(3, -3)},
                          0: {'point_2': Point(1, 1), 'point_3': Point(2, 2), 'point_4': Point(3, 3)}},
              'piece_2': {1: {'point_2': Point(-1, -1), 'point_3': Point(-2, -2), 'point_4': Point(-3, -1)},
                          2: {'point_2': Point(1, -1), 'point_3': Point(2, -2), 'point_4': Point(1, -3)},
                          3: {'point_2': Point(1, 1), 'point_3': Point(2, 2), 'point_4': Point(3, 1)},
                          0: {'point_2': Point(-1, 1), 'point_3': Point(-2, 2), 'point_4': Point(-1, 3)}},
              'piece_3': {1: {'point_2': Point(1, 3), 'point_3': Point(0, 2), 'point_4': Point(-1, 1)},
                          2: {'point_2': Point(-3, 1), 'point_3': Point(-2, 0), 'point_4': Point(-1, -1)},
                          3: {'point_2': Point(-1, -3), 'point_3': Point(0, -2), 'point_4': Point(1, -1)},
                          0: {'point_2': Point(3, -1), 'point_3': Point(2, 0), 'point_4': Point(1, 1)}},
              'piece_4': {1: {'point_2': Point(-1, -1), 'point_3': Point(0, 2), 'point_4': Point(-1, 1)},
                          2: {'point_2': Point(1, -1), 'point_3': Point(-2, 0), 'point_4': Point(-1, -1)},
                          3: {'point_2': Point(1, 1), 'point_3': Point(0, -2), 'point_4': Point(1, -1)},
                          0: {'point_2': Point(-1, 1), 'point_3': Point(2, 0), 'point_4': Point(1, 1)}},
              'piece_5': {1: {'point_2': Point(-1, -1), 'point_3': Point(-1, 1), 'point_4': Point(-2, 0)},
                          2: {'point_2': Point(1, -1), 'point_3': Point(-1, -1), 'point_4': Point(0, -2)},
                          3: {'point_2': Point(1, 1), 'point_3': Point(1, -1), 'point_4': Point(2, 0)},
                          0: {'point_2': Point(-1, 1), 'point_3': Point(1, 1), 'point_4': Point(0, 2)}}}
    move_space = {'all': Point(0, 1)}


class Move:
    def __init__(self, piece: Piece, board_left_up, board_left_down, board_right_up, board_right_down):
        self._piece = piece
        self._board_left_up = board_left_up
        self._board_left_down = board_left_down
        self._board_right_up = board_right_up
        self._board_right_down = board_right_down
        self.__clockwise_movement = 0
        self.__anti_clockwise_movement = 0

    def is_valid_piece_move(self, move_type):
        move = move_type.value
        move_name = move_type.name
        point_1 = self._piece.point_1
        point_2 = self._piece.point_2
        point_3 = self._piece.point_3
        point_4 = self._piece.point_4
        if 'all' in move:
            point_1 = point_1 + move['all']
            if point_1.less() or point_1.greater():
                return False
            point_2 = point_2 + move['all']
            if point_2.less() or point_2.greater():
                return False
            point_3 = point_3 + move['all']
            if point_3.less() or point_3.greater():
                return False
            point_4 = point_4 + move['all']
            if point_4.less() or point_4.greater():
                return False
        else:
            piece_name = self._piece.piece_type.name
            if move_name == "move_w":
                rotation_movement = self.__anti_clockwise_movement + 1
            else:
                rotation_movement = self.__clockwise_movement + 1
            rotation_movement %= 4
            point_1 = point_1 + Point(0, 1)
            if point_1.less() or point_1.greater():
                return False
            point_2 = point_2 + move[piece_name][rotation_movement]['point_2'] + Point(0, 1)
            if point_2.less() or point_2.greater():
                return False
            point_3 = point_3 + move[piece_name][rotation_movement]['point_3'] + Point(0, 1)
            if point_3.less() or point_3.greater():
                return False
            point_4 = point_4 + move[piece_name][rotation_movement]['point_4'] + Point(0, 1)
            if point_4.less() or point_4.greater():
                return False
            if move_name == "move_w":
                self.__anti_clockwise_movement += 1
                self.__anti_clockwise_movement %= 4
            else:
                self.__clockwise_movement += 1
                self.__clockwise_movement %= 4
        return True

    def move_piece(self, move_type):
        if not self.is_valid_piece_move(move_type):
            print("Please Select some other move, .. this is not a valid move .......\n")
            return False
        move = move_type.value
        move_name = move_type.name
        point_1 = self._piece.point_1
        point_2 = self._piece.point_2
        point_3 = self._piece.point_3
        point_4 = self._piece.point_4
        if 'all' in move:
            self._piece.update_point_1(point_1 + move['all'])
            self._piece.update_point_2(point_2 + move['all'])
            self._piece.update_point_3(point_3 + move['all'])
            self._piece.update_point_4(point_4 + move['all'])
        else:
            piece_name = self._piece.piece_type.name
            if move_name == "move_w":
                rotation_movement = self.__anti_clockwise_movement
            else:
                rotation_movement = self.__clockwise_movement
            self._piece.update_point_1(point_1 + Point(0, 1))
            self._piece.update_point_2(point_2 + move[piece_name][rotation_movement]['point_2'] + Point(0, 1))
            self._piece.update_point_3(point_3 + move[piece_name][rotation_movement]['point_3'] + Point(0, 1))
            self._piece.update_point_4(point_4 + move[piece_name][rotation_movement]['point_4'] + Point(0, 1))
        return True

    def get_piece(self):
        return self._piece


def test_is_valid_piece_move():
    move_1 = Move(Piece(PieceType.piece_1), Point(0, 1), Point(0, 13), Point(13, 1), Point(13, 13))
    assert move_1.is_valid_piece_move(MoveType.move_d) is True
    assert move_1.is_valid_piece_move(MoveType.move_w) is False
    move_1.move_piece(MoveType.move_a)
    assert move_1.get_piece().point_1.x == 4
    assert move_1.get_piece().point_1.y == 2
    assert move_1.get_piece().point_2.x == 5
    assert move_1.get_piece().point_3.x == 6
    assert move_1.get_piece().point_4.x == 7
    move_1.move_piece(MoveType.move_s)
    assert move_1.get_piece().point_1.y == 3
    assert move_1.get_piece().point_2.x == 4
    assert move_1.get_piece().point_3.y == 5
    assert move_1.get_piece().point_4.y == 6


