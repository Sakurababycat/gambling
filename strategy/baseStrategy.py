from strategy import Register, RegisterDecorator
from typing import Callable, Generic, Type, TypeVar
import sys
from enum import Enum
from abc import abstractmethod

if sys.version_info > (3, 12):
    from typing import override
else:

    def override(func):
        return func


class BaseStrategy(RegisterDecorator):
    class RegisterCallingMessage(Enum):
        Registed = "StrategyRegister"

    def __init__(self) -> None:
        raise NotImplementedError("BaseStrategy is an abstract class")

    @abstractmethod
    def step(self, lh: list[bool], rh: list[bool]):
        pass

    @classmethod
    def _makeStrategy(cls, name=None, *args, **kwargs) -> dict[str, "BaseStrategy"]:
        name = name if name else cls.__name__
        return {name: StrategyRegister[cls.__name__](*args, **kwargs)}

    @classmethod
    def makeStrategy(cls) -> dict[str, "BaseStrategy"]:
        return cls._makeStrategy()


T = TypeVar("T", bound=BaseStrategy)


class StrategyRegister(Register, Generic[T]):
    @override
    @classmethod
    def __getitem__(cls, key: str) -> Callable[..., Type[T]]:
        return BaseStrategy.callFromRegister(cls.get_dict()[key])
