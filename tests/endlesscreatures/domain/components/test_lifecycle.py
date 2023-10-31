import pytest
from endlesscreatures.domain.components.lifecycle import LifeCycle
from endlesscreatures.domain.protocols.lifecycle_user import LifeCycleUser


class MockLifeCycleUser(LifeCycleUser):
    def __init__(self):
        self.energy = 0
        self.current_age = 0
        self.location = None
        self.reproductions = 0

    def begin_life(self, energy, age, location):
        self.energy = energy
        self.current_age = age
        self.location = location

    def age(self, years):
        self.current_age += years
        self.energy -= years * 2

    def end_life(self):
        self.energy = 0

    def reproduce(self):
        self.reproductions += 1
        self.energy -= 10  # Energia gasta durante a reprodução


@pytest.fixture
def mock_lifecycle_user():
    return MockLifeCycleUser()


@pytest.fixture
def lifecycle_component(mock_lifecycle_user):
    return LifeCycle(user=mock_lifecycle_user)


class TestLifeCycleComponent:
    def test_begin_life(self, lifecycle_component, mock_lifecycle_user):
        lifecycle_component.begin_life(100, 0, 'forest')
        assert mock_lifecycle_user.energy == 100
        assert mock_lifecycle_user.current_age == 0
        assert mock_lifecycle_user.location == 'forest'

    def test_age(self, lifecycle_component, mock_lifecycle_user):
        mock_lifecycle_user.energy = 100
        mock_lifecycle_user.current_age = 10
        lifecycle_component.age(5)
        assert mock_lifecycle_user.current_age == 15
        assert mock_lifecycle_user.energy == 90  # 100 - 5*2

    def test_end_life(self, lifecycle_component, mock_lifecycle_user):
        lifecycle_component.end_life()
        assert mock_lifecycle_user.energy == 0

    def test_reproduce(self, lifecycle_component, mock_lifecycle_user):
        mock_lifecycle_user.energy = 50
        lifecycle_component.reproduce()
        assert mock_lifecycle_user.reproductions == 1
        assert mock_lifecycle_user.energy == 40  # 50 - 10
