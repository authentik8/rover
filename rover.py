import sys

class Rover:

    compass = ['N', 'E', 'S', 'W']

    def __init__(self, x=0, y=0, direction='N', grid_x=50, grid_y=50, obstacles=None):
        self.x = x
        self.y = y
        self.direction = direction

        self.grid_x = grid_x
        self.grid_y = grid_y

        if obstacles is None:
            obstacles = []

        self.obstacles = obstacles

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

    def obstacle_at_position(self, x, y):
        for obstacle in self.obstacles:
            if obstacle[0] == x and obstacle[1] == y:
                return True

        return False

    def move(self, command_string, out=sys.stdout):
        for command in command_string:

            new_x = self.x
            new_y = self.y

            if command == 'F':
                # Move forward command
                if self.axis == 0:
                    # Working on X axis
                    new_x = (self.x + 1 * self.multiplier) % self.grid_x
                else:
                    # Working on Y axis
                    new_y = (self.y + 1 * self.multiplier) % self.grid_y
            elif command == 'B':
                # Move backwards command
                if self.axis == 0:
                    # Working on X axis
                    new_x = (self.x - 1 * self.multiplier) % self.grid_x
                else:
                    # Working on Y axis
                    new_y = (self.y - 1 * self.multiplier) % self.grid_y

            elif command == 'R':
                # Rotate right
                new_index = (self.compass_index + 1) % 4
                self.direction = self.compass[new_index]

            elif command == 'L':
                # Rotate left
                new_index = (self.compass_index - 1) % 4
                self.direction = self.compass[new_index]

            if not self.obstacle_at_position(new_x, new_y):
                self.x = new_x
                self.y = new_y
            else:
                out.write(
                    "Obstacle encountered while attempting to move to "
                    "({new_x}, {new_y}) from ({x}, {y})".format(new_x=new_x,
                                                                new_y=new_y,
                                                                x=self.x,
                                                                y=self.y)
                )
                break
