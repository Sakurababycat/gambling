from strategy import StrategyRegister, BaseStrategy, override


@StrategyRegister
class FriedMan(BaseStrategy):
    def __init__(self):
        self.defected = False

    @override
    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        if not rh:
            self.defected = False
        if rh and (rh[-1] == False):
            self.defected = True
        return not self.defected
