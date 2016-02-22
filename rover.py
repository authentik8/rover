class Rover:

    compass = ['N', 'E', 'S', 'W']

    def __init__(self, x=0, y=0, direction='N'):
        self.x = x
        self.y = y
        self.direction = direction

    @property
    def position(self):
        return self.x, self.y, self.direction

    def set_position(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
