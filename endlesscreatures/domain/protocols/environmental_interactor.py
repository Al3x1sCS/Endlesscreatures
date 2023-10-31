from typing import Protocol


class EnvironmentalInteractor(Protocol):
    def interact_with_env(self) -> None:
        ...
