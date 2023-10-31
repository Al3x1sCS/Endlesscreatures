from __future__ import annotations

from typing import Type
from endlesscreatures.domain.protocols.energy_user import EnergyUser


class EnergyComponent:
    def __init__(self, user: Type[EnergyUser], initial_energy: float = 0.0):
        self._user = user
        self._energy = initial_energy

    def gain_energy(self, amount: float) -> None:
        self._energy += amount
        self._user.gain_energy(amount)

    def expend_energy(self, amount: float) -> None:
        self._energy -= amount
        self._user.expend_energy(amount)
