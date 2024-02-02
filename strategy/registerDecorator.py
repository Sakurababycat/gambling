from typing import Any, final, Callable
from enum import Enum
import sys

if sys.version_info > (3, 12):
    from typing import override
else:
    def override(func): return func


def bound_method_deco(func, instance):
    def wrapper(*args, **kwargs):
        return func(instance, *args, **kwargs)
    return wrapper


class RegisterDecoratorMeta(type):
    def __call__(cls, callMsg: str = None, *args, **kwargs):

        if not callMsg is cls.RegisterCallingMessage.Registed:
            raise AssertionError(
                f"{cls.__name__} can only be called by {cls.RegisterCallingMessage.Registed.value}")
        # 判断是否通过Register调用
        return super().__call__(*args, **kwargs)


class RegisterDecorator(metaclass=RegisterDecoratorMeta):
    class RegisterCallingMessage(Enum):
        Registed = "Register"

    def __init__(self) -> None:
        raise NotImplementedError("RegisterDecorator is an abstract class")

    @final
    @classmethod
    def callFromRegister(cls, call: Callable[[RegisterCallingMessage, Any], Any]) -> Callable[..., Any]:
        return lambda *args, **kwargs: call(cls.RegisterCallingMessage.Registed, *args, **kwargs)
