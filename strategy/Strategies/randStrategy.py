from strategy import StrategyRegister, BaseStrategy, override
from random import random

from strategy.baseStrategy import BaseStrategy


@StrategyRegister
class Rand(BaseStrategy):
    def __init__(self, cooprate=0.5):
        self.cooprate = cooprate

    @override
    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        return random() < self.cooprate

    @override
    @classmethod
    def makeStrategy(cls) -> dict[str, "BaseStrategy"]:
        dic = {}
        for rate in range(5, 6, 3):
            dic.update(cls._makeStrategy(f"Rand_{rate}", rate / 10))
        return dic
