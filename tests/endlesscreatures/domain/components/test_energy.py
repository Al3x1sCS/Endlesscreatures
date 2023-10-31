import pytest
from endlesscreatures.domain.components.energy import EnergyComponent
from endlesscreatures.domain.protocols.energy_user import EnergyUser


class MockEnergyUser(EnergyUser):
    def __init__(self):
        self.energy_gained = 0
        self.energy_expended = 0

    def gain_energy(self, amount: float) -> None:
        self.energy_gained += amount

    def expend_energy(self, amount: float) -> None:
        self.energy_expended += amount


@pytest.fixture
def mock_user():
    return MockEnergyUser()


@pytest.fixture
def energy_component(mock_user):
    return EnergyComponent(user=mock_user, initial_energy=50.0)


class TestEnergyComponent:
    def test_gain_energy(self, energy_component, mock_user):
        energy_component.gain_energy(10.0)
        assert energy_component._energy == 60.0
        assert mock_user.energy_gained == 10.0

    def test_expend_energy(self, energy_component, mock_user):
        energy_component.expend_energy(20.0)
        assert energy_component._energy == 30.0
        assert mock_user.energy_expended == 20.0
