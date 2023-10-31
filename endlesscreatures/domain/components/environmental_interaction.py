from __future__ import annotations

from typing import Type
from endlesscreatures.domain.protocols.environmental_interactor import EnvironmentalInteractor


class EnvironmentalInteraction:
    def __init__(self, interactor: Type[EnvironmentalInteractor]):
        self._interactor = interactor

    def interact_with_env(self) -> None:
        self._interactor.interact_with_env()
