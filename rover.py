class Rover:

    compass = ['N', 'E', 'S', 'W']

    def __init__(self, x=0, y=0, direction='N'):
        self.x = x
        self.y = y
        self.direction = direction

    @property
    def position(self):
        return self.x, self.y, self.direction

    @property
    def compass_index(self):
        return next(i for i in range(0, len(self.compass)) if self.compass[i] == self.direction)


    @property
    def axis(self):
        # 0 if pointing along x axis
        # 1 if pointing along y axis
        return (self.compass_index + 1) % 2

    def set_position(self, x=None, y=None, direction=None):
          if x is not None:
              self.x = x

          if y is not None:
              self.y = y

          if direction is not None:
              self.direction = direction

    def move(self, *args):
        for command in args:
            if command == 'F':
                # Move forward command
                if self.compass_index < 2:
                    # Upper right quadrant, increasing x/y
                    pass
            else:
                pass
