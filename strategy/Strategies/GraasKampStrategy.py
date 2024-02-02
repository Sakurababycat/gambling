from strategy import StrategyRegister, BaseStrategy, override


@StrategyRegister
class GraasKamp(BaseStrategy):
    def __init__(self):
        ...

    @override
    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        if len(rh) < 2:
            return True
        elif len(rh) % 50 == 0:
            return False
        else:
            return not lh[-2] and rh[-1] and rh[-2]
