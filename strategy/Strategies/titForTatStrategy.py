from strategy import StrategyRegister, BaseStrategy, override


@StrategyRegister
class TitForTat(BaseStrategy):
    def __init__(self):
        ...

    @override
    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        if not rh:
            return True
        else:
            return rh[-1]
