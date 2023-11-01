import pytest
from endlesscreatures.domain.components.movement import Movement
from endlesscreatures.domain.protocols.movement_user import MovementUser


class MockMovementUser(MovementUser):
    def __init__(self):
        self.distance_moved = 0
        self.stopped = False

    def move(self, distance: float) -> None:
        self.distance_moved += distance

    def stop(self) -> None:
        self.stopped = True


@pytest.fixture
def mock_movement_user():
    return MockMovementUser()


@pytest.fixture
def movement_component(mock_movement_user):
    return Movement(user=mock_movement_user)


class TestMovementComponent:
    def test_move(self, movement_component, mock_movement_user):
        movement_component.move(5.0)
        assert mock_movement_user.distance_moved == 5.0

    def test_stop(self, movement_component, mock_movement_user):
        movement_component.stop()
        assert mock_movement_user.stopped == True
