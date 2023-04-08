from enum import Enum
from point import Point


class PieceType(Enum):
    piece_1 = {'point_1': Point(5, 1), 'point_2': Point(6, 1), 'point_3': Point(7, 1), 'point_4': Point(8, 1)}
    piece_2 = {'point_1': Point(6, 1), 'point_2': Point(6, 2), 'point_3': Point(6, 3), 'point_4': Point(7, 3)}
    piece_3 = {'point_1': Point(6, 3), 'point_2': Point(7, 1), 'point_3': Point(7, 2), 'point_4': Point(7, 3)}
    piece_4 = {'point_1': Point(6, 2), 'point_2': Point(6, 3), 'point_3': Point(7, 1), 'point_4': Point(7, 2)}
    piece_5 = {'point_1': Point(6, 1), 'point_2': Point(6, 2), 'point_3': Point(7, 1), 'point_4': Point(7, 2)}


class Piece:
    def __init__(self, piece_type: PieceType):
        self._piece_type = piece_type
        piece_value = self._piece_type.value
        self._point_1 = piece_value['point_1']
        self._point_2 = piece_value['point_2']
        self._point_3 = piece_value['point_3']
        self._point_4 = piece_value['point_4']

    @property
    def point_1(self):
        return self._point_1

    @property
    def point_2(self):
        return self._point_2

    @property
    def point_3(self):
        return self._point_3

    @property
    def point_4(self):
        return self._point_4

    @property
    def piece_tye(self):
        return self._piece_type

    def update_point_1(self, point):
        self._point_1 = point

    def update_point_2(self, point):
        self._point_2 = point

    def update_point_3(self, point):
        self._point_3 = point

    def update_point_4(self, point):
        self._point_4 = point


if __name__ == "__main__":
    first_piece = Piece(PieceType.piece_1)