from policy import Register, RegisterDecorator
from typing import Callable, Generic, Type, TypeVar
import sys
from enum import Enum
from abc import abstractmethod

if sys.version_info > (3, 12):
    from typing import override
else:

    def override(func):
        return func


class BasePolicy(RegisterDecorator):
    class RegisterCallingMessage(Enum):
        Registed = "PolicyRegister"

    def __init__(self) -> None:
        raise NotImplementedError("BasePolicy is an abstract class")

    @abstractmethod
    def step(self, lh: list[bool], rh: list[bool]):
        pass

    @classmethod
    def _makePolicy(cls, name=None, *args, **kwargs) -> "BasePolicy":
        name = name if name else cls.__name__
        return (name, PolicyRegister[cls.__name__](*args, **kwargs))

    @classmethod
    def makePolicy(cls):
        return cls._makePolicy()


T = TypeVar("T", bound=BasePolicy)


class PolicyRegister(Register, Generic[T]):
    @override
    @classmethod
    def __getitem__(cls, key: str) -> Callable[..., Type[T]]:
        return BasePolicy.callFromRegister(cls.get_dict()[key])
