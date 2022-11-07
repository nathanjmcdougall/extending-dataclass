"""A Descriptor for object access.
"""

class GetFrom:
    """A Descriptor for object access.

    For example,
    ```
    class A:
        x: int  = 1

    @dataclass
    class B:
        a: A
        x: int = GetFrom("a", "x")
    ```
    Would allow access to `b.a.x` as `b.x`.
    """

    def __init__(self, *attrs):
        self.attrs = attrs

    def __get__(self, obj, objtype=None):
        this = obj
        for attr in self.attrs:
            this = getattr(this, attr)
        return this
