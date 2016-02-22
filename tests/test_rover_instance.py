
from unittest import TestCase
from rover import Rover

class TestRover(TestCase):

    compass_headings = ['N', 'E', 'S', 'W']

    def setUp(self):
        self.rover = Rover()

    def test_rover_compass(self):
        assert self.rover.compass == self.compass_headings

    def test_rover_position(self):
        assert self.rover.position == (self.rover.x, self.rover.y, self.rover.direction)

    def test_rover_set_position(self):
        self.rover.set_position(4, 9, 'W')
        assert self.rover.position == (4, 9, 'W')

    def test_rover_compass_index(self):
        for i in range(0, len(self.compass_headings)):
            self.rover.direction = self.compass_headings[i]
            assert self.rover.compass_index == i

    def test_rover_axis(self):
        for i in range(0, len(self.compass_headings)):
            self.rover.direction = self.compass_headings[i]
            if self.rover.direction in ['E', 'W']:
                assert self.rover.axis == 0
            else:
                assert self.rover.axis == 1

    def test_rover_multiplier(self):
        for i in range(0, len(self.compass_headings)):
            self.rover.direction = self.compass_headings[i]
            if self.rover.direction in ['N', 'E']:
                assert self.rover.multiplier == 1
            else:
                assert self.rover.multiplier == -1

    def test_rover_move_forward_north(self):
        self.rover.set_position(0, 0, 'N')
        self.rover.move('F')
        assert self.rover.position == (0, 1, 'N')

    def test_rover_move_forward_south(self):
        self.rover.set_position(0, 1, 'S')
        self.rover.move('F')
        assert self.rover.position == (0, 0, 'S')

    def test_rover_move_forward_east(self):
        self.rover.set_position(0, 0, 'E')
        self.rover.move('F')
        assert self.rover.position == (1, 0, 'E')

    def test_rover_move_forward_west(self):
        self.rover.set_position(1, 0, 'W')
        self.rover.move('F')
        assert self.rover.position == (0, 0, 'W')
