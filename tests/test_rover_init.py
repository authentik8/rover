def test_rover_init_with_default_parameters():
    from rover import Rover
    rover = Rover()
    assert rover.x == 0
    assert rover.y == 0
    assert rover.direction == 'N'

    assert rover.grid_x == 50
    assert rover.grid_y == 50

    assert rover.obstacles == []

def test_rover_init_with_custom_parameters():
    from rover import Rover
    rover = Rover(3, 7, 'W')
    assert rover.x == 3
    assert rover.y == 7
    assert rover.direction == 'W'

    assert rover.grid_x == 50
    assert rover.grid_y == 50

    assert rover.obstacles == []


def test_rover_init_custom_grid():
    from rover import Rover
    rover = Rover(grid_x=100, grid_y=150)
    assert rover.x == 0
    assert rover.y == 0
    assert rover.direction == 'N'

    assert rover.grid_x == 100
    assert rover.grid_y == 150

    assert rover.obstacles == []


def test_rover_init_full_custom_grid():
    from rover import Rover
    rover = Rover(5, 9, 'E', 100, 150)
    assert rover.x == 5
    assert rover.y == 9
    assert rover.direction == 'E'

    assert rover.grid_x == 100
    assert rover.grid_y == 150

    assert rover.obstacles == []

def test_rover_init_obstacles():
    from rover import Rover
    rover = Rover(25, 91, 'S', 100, 150, [(23, 97), (54, 71)])
    assert rover.x == 25
    assert rover.y == 91
    assert rover.direction == 'S'

    assert rover.grid_x == 100
    assert rover.grid_y == 150

    assert rover.obstacles == [(23, 97), (54, 71)]
