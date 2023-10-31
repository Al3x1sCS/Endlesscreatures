import pytest
from endlesscreatures.domain.components.environmental_interaction import EnvironmentalInteraction
from endlesscreatures.domain.protocols.environmental_interactor import EnvironmentalInteractor


class MockEnvironmentalInteractor(EnvironmentalInteractor):
    def __init__(self):
        self.interactions = 0

    def interact_with_env(self):
        self.interactions += 1


@pytest.fixture
def mock_interactor():
    return MockEnvironmentalInteractor()


@pytest.fixture
def environmental_component(mock_interactor):
    return EnvironmentalInteraction(interactor=mock_interactor)


class TestEnvironmentalInteraction:
    def test_basic_interaction(self, environmental_component, mock_interactor):
        environmental_component.interact_with_env()
        assert mock_interactor.interactions == 1
