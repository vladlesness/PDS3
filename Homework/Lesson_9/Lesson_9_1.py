class Car1:
    def __init__(self, brand, engine, color):
        self.brand = brand
        self.engine = engine
        self.color = color

    @staticmethod
    def go_forward(self):
        print(f'Your {self.brand} goes forward')

    @staticmethod
    def go_backward(self):
        print(f'Your {self.brand} goes backward')


class Car2(Car1):
    @staticmethod
    def go_right(self):
        print(f'Your {self.brand} goes right')

    @staticmethod
    def go_left(self):
        print(f'Your {self.brand} goes left')
