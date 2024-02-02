from strategy import StrategyRegister, BaseStrategy, override


@StrategyRegister
class Kind(BaseStrategy):
    def __init__(self):
        ...

    @override
    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        return True
