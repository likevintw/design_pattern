


class

class Factory():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shift = 20
    def draw(self):
        raise NotImplementedError()
    def move(self, direction):
        if direction == 'up':
            self.y -= self.shift
        elif direction == 'down':
            self.y += self.shift
        elif direction == 'left':
            self.x -= self.shift
        elif direction == 'right':
            self.x += self.shift
    @staticmethod
    def factory(_type):
        if _type == "circle": return Circle(100, 100)
        if _type == "square": return Square(100, 100)
        return None

