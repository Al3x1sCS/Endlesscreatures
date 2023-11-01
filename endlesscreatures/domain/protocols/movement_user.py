from typing import Protocol


class MovementUser(Protocol):
    def move(self, distance: float) -> None:
        ...

    def stop(self) -> None:
        ...
