from dataclasses import dataclass, field
from get_from import GetFrom


@dataclass(frozen=True, kw_only=True)
class MyClass:
    a: int
    b: int
    c: int


def _from_myclass(attr, **kwargs):
    return field(default=GetFrom("my_class", attr), **kwargs)


@dataclass(frozen=True, kw_only=True)
class MyExtendedClass:
    my_class: MyClass = field(repr=False)
    a: int = _from_myclass("a", repr=True, init=False)
    b: int = _from_myclass("b", repr=True, init=False)
    c: int = _from_myclass("c", repr=True, init=False)
    d: int = field()
    e: int = field()


if __name__ == "__main__":
    my_class = MyClass(a=1, b=2, c=3)
    my_extended_class = MyExtendedClass(my_class=my_class, d=4, e=5)
    print(my_extended_class)
