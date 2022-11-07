from dataclasses import dataclass, asdict


@dataclass(frozen=True, kw_only=True)
class MyClass:
    a: int
    b: int
    c: int

    @classmethod
    def extend(cls, my_class, **kwargs):
        """This function may better live in MyExtendedClass.

        The reason it might be better here is just if you plan to extend MyClass
        multiple times. In that case, you can just call this function from all
        the subclasses.
        """
        return cls(**asdict(my_class), **kwargs)


@dataclass(frozen=True, kw_only=True)
class MyExtendedClass(MyClass):
    d: int
    e: int


if __name__ == "__main__":
    my_class = MyClass(a=1, b=2, c=3)
    my_extended_class = MyExtendedClass.extend(my_class, d=4, e=5)
    print(my_extended_class)
