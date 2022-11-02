class Parallelogram:
    def __int__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height


class Square(Parallelogram):
    def get_area(self):
        return self.base ** 2
