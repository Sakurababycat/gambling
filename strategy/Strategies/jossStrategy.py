from strategy import StrategyRegister, BaseStrategy, override
from random import random


@StrategyRegister
class Joss(BaseStrategy):
    def __init__(self):
        ...

    @override
    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        if not rh:
            return True
        else:
            return rh[-1] and random() > 0.1
