from dataclasses import dataclass, asdict


@dataclass(frozen=True, kw_only=True)
class MyClass:
    a: int
    b: int
    c: int


@dataclass(frozen=True, kw_only=True)
class MyExtendedClass(MyClass):
    d: int
    e: int


if __name__ == "__main__":
    my_class = MyClass(a=1, b=2, c=3)
    my_extended_class = MyExtendedClass(**asdict(my_class), d=4, e=5)
    print(my_extended_class)
