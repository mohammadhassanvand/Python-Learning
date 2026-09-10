def fact(n):
    f = 1
    for i in range(1, n+1):
        f = i * f
    return(f)

print(fact(17))
from abc import ABC, abstractmethod


class f(ABC):
    """Concrete implementation of an abstract interface providing
    simple numeric utilities."""

    @abstractmethod
    def compute(self, n: int) -> int:
        """Compute a value from n."""

    @abstractmethod
    def describe(self, n: int) -> str:
        """Return a short description of the computation."""


class f(f):
    """Implementation of abstract methods: compute returns factorial using
    the module-level fact function; describe returns a brief summary."""

    def compute(self, n: int) -> int:
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer")
        return fact(n)

    def describe(self, n: int) -> str:
        return f"factorial({n}) = {self.compute(n)}"


__all__ = ["fact", "f"]

