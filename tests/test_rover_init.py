def test_rover_init_with_default_parameters():
    from rover import Rover
    rover = Rover()
    assert rover.x == 0
    assert rover.y == 0
    assert rover.direction == 'N'

def test_rover_init_with_custom_paramaters():
    from rover import Rover
    rover = Rover(3, 7, 'W')
    assert rover.x == 3
    assert rover.y == 7
    assert rover.direction == 'W'
