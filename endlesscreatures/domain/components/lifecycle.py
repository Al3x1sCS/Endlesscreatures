from __future__ import annotations

from typing import Type
from endlesscreatures.domain.protocols.lifecycle_user import LifeCycleUser


class LifeCycle:
    def __init__(self, user: Type[LifeCycleUser]):
        self._user = user

    def begin_life(self, energy: float, age: int, location: str) -> None:
        self._user.begin_life(energy, age, location)

    def age(self, years: int) -> None:
        self._user.age(years)

    def end_life(self) -> None:
        self._user.end_life()

    def reproduce(self) -> None:
        self._user.reproduce()
