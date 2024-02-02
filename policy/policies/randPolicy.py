from policy import PolicyRegister, BasePolicy, override
from random import random

from policy.basePolicy import BasePolicy


@PolicyRegister.register
class Rand(BasePolicy):
    def __init__(self, cooprate=0.5):
        self.cooprate = cooprate

    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        return random > self.cooprate

    @override
    @classmethod
    def makePolicy(cls) -> BasePolicy:
        for rate in range(1, 10):
            yield cls._makePolicy(f"Rand_{rate}", rate / 10)
