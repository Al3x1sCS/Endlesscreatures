from typing import Protocol


class LifeCycleUser(Protocol):
    def begin_life(self, energy: float, age: int, location: str) -> None:
        ...

    def age(self, years: int) -> None:
        ...

    def end_life(self) -> None:
        ...

    def reproduce(self) -> None:
        ...
