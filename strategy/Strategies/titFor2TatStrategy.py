from strategy import StrategyRegister, BaseStrategy, override


@StrategyRegister
class TitFor2Tat(BaseStrategy):
    def __init__(self):
        ...

    @override
    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        if len(rh) < 2:
            return True
        else:
            return rh[-1] or rh[-2]
