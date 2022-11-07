from dataclasses import dataclass, asdict
from get_from import GetFrom


@dataclass(frozen=True, kw_only=True)
class MyClass:
    a: int
    b: int
    c: int


@dataclass(frozen=True, kw_only=True)
class MyExtendedClass:
    a: int
    b: int
    c: int
    d: int
    e: int

    @classmethod
    def extend(cls, my_class, **kwargs):
        return cls(**asdict(my_class), **kwargs)


if __name__ == "__main__":
    my_class = MyClass(a=1, b=2, c=3)
    my_extended_class = MyExtendedClass.extend(my_class, d=4, e=5)
    print(my_extended_class)
