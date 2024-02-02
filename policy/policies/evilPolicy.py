from policy import PolicyRegister, BasePolicy


@PolicyRegister.register
class Evil(BasePolicy):
    def __init__(self):
        ...

    def step(self, lh: list[bool], rh: list[bool]) -> bool:
        return False
