from policy import PolicyRegister, BasePolicy
from random import randint


@PolicyRegister.register
class Rand(BasePolicy):
    def __init__(self):
        ...

    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        return bool(randint(0, 1))
