from policy import PolicyRegister, BasePolicy
from random import random


@PolicyRegister.register
class Rand(BasePolicy):
    def __init__(self, cooprate=0.5):
        self.cooprate = cooprate

    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        return random > self.cooprate
