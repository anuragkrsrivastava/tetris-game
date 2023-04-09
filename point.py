class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # add dunder
    def __add__(self, other_point):
        x = self.x + other_point.x
        y = self.y + other_point.y
        return Point(x, y)

    def less(self):
        if self.x <= 0 or self.y <= 0:
            return True
        return False

    def greater(self):
        if self.y > 12 or self.x > 12:
            return True
        return False

