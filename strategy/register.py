from typing import Callable, Generic, Type, TypeVar, TypeAlias, Any, final

T = TypeVar("T")


class RegisterMeta(type):
    def __getitem__(cls, key: str) -> Type[T] | Callable[..., Any]:
        return cls.__getitem__(key)

    def __str__(cls) -> str:
        return cls.__str__()

    def __contains__(cls, key: str) -> bool:
        return cls.__contains__(key)

    def __setitem__(cls, key: str, value: Type[T] | Callable[..., Any]) -> None:
        cls.__setitem__(key, value)

    def __call__(cls, target: Type[T] | Callable[..., Any] | str):
        return cls.register(target)


class Register(Generic[T], metaclass=RegisterMeta):
    _dict: dict[str, Type[T] | Callable[..., Any]] = None

    @final
    @classmethod
    def get_dict(cls) -> dict[str, Type[T] | Callable[..., Any]]:
        if cls._dict is None:
            cls._dict = {}
        return cls._dict

    @classmethod
    def add_item(
        cls, key: str, value: Type[T] | Callable[..., Any]
    ) -> Type[T] | Callable[..., Any]:
        if not callable(value):
            raise Exception(f"Error:{value} must be callable!")
        if key in cls:
            print(
                f"\033[31m[Warning]:\033[0m {key} already exists and will be overwritten!"
            )
        cls[key] = value
        return value

    @classmethod
    def register(
        cls, target: Type[T] | Callable[..., Any] | str
    ) -> (
        Type[T]
        | Callable[..., Any]
        | Callable[[Type[T] | Callable[..., Any]], Type[T] | Callable[..., Any]]
    ):
        if callable(target):  # 传入的target可调用 --> 没有给注册名 --> 传入的函数名或类名作为注册名
            return cls.add_item(target.__name__, target)
        else:  # 不可调用 --> 传入了注册名 --> 作为可调用对象的注册名
            return lambda x: cls.add_item(target, x)

    @classmethod
    def __setitem__(cls, key: str, value: Type[T] | Callable[..., Any]):
        cls.get_dict()[key] = value

    @classmethod
    def __getitem__(cls, key: str) -> Type[T] | Callable[..., Any]:
        return cls.get_dict()[key]

    @classmethod
    def __contains__(cls, key: str):
        return key in cls.get_dict()

    @classmethod
    def __str__(cls):
        return str(cls.get_dict())

    @classmethod
    def keys(cls):
        return cls.get_dict().keys()

    @classmethod
    def values(cls):
        return cls.get_dict().values()

    @classmethod
    def items(cls):
        return cls.get_dict().items()


if __name__ == "__main__":

    @Register.register("f1")
    def func():
        pass

    @Register.register
    def func():
        pass

    @Register
    def func():
        pass

    @Register("f3")
    def func():
        pass

    print(Register["f1"])
    print(Register)
