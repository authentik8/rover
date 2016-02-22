
from unittest import TestCase
from rover import Rover

class TestRover(TestCase):

    def setUp(self):
        self.rover = Rover()

    def test_rover_compass(self):
        assert self.rover.compass == ['N', 'E', 'S', 'W']
