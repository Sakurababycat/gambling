from policy import PolicyRegister, BasePolicy


@PolicyRegister.register
class Kind(BasePolicy):
    def __init__(self):
        ...

    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        return True
