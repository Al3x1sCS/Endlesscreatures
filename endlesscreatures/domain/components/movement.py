from __future__ import annotations

from typing import Type
from endlesscreatures.domain.protocols.movement_user import MovementUser


class Movement:
    def __init__(self, user: Type[MovementUser]):
        self._user = user

    def move(self, distance: float) -> None:
        self._user.move(distance)

    def stop(self) -> None:
        self._user.stop()
