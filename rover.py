class Rover:

    compass = ['N', 'E', 'S', 'W']

    def __init__(self, x=0, y=0, direction='N', grid_x=50, grid_y=50):
        self.x = x
        self.y = y
        self.direction = direction

        self.grid_x = grid_x
        self.grid_y = grid_y

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

    @property
    def multiplier(self):
        # 1 if pointing N or E
        # -1 if pointing S or W
        if self.compass_index <= 1:
            return 1
        else:
            return -1

    def set_position(self, x=None, y=None, direction=None):
          if x is not None:
              self.x = x

          if y is not None:
              self.y = y

          if direction is not None:
              self.direction = direction

    def move(self, command_string):
        for command in command_string:
            if command == 'F':
                # Move forward command
                if self.axis == 0:
                    # Working on X axis
                    self.x = (self.x + 1 * self.multiplier) % self.grid_x
                else:
                    # Working on Y axis
                    self.y = (self.y + 1 * self.multiplier) % self.grid_y
            elif command == 'B':
                # Move backwards command
                if self.axis == 0:
                    # Working on X axis
                    self.x = (self.x - 1 * self.multiplier) % self.grid_x
                else:
                    # Working on Y axis
                    self.y = (self.y - 1 * self.multiplier) % self.grid_y

            elif command == 'R':
                # Rotate right
                new_index = (self.compass_index + 1) % 4
                self.direction = self.compass[new_index]

            elif command == 'L':
                # Rotate left
                new_index = (self.compass_index - 1) % 4
                self.direction = self.compass[new_index]
