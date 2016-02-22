
from unittest import TestCase
from rover import Rover

class TestRover(TestCase):

    def setUp(self):
        self.rover = Rover()

    def test_rover_compass(self):
        assert self.rover.compass == ['N', 'E', 'S', 'W']

    def test_rover_position(self):
        assert self.rover.position == (self.rover.x, self.rover.y, self.rover.direction)

    def test_rover_set_position(self):
        self.rover.set_position(4, 9, 'W')
        assert self.rover.position == (4, 9, 'W')

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
