
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
