from typing import Protocol


class EnergyUser(Protocol):
    def gain_energy(self, amount: float) -> None:
        ...

    def expend_energy(self, amount: float) -> None:
        ...
