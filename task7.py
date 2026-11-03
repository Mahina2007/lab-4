# Task 7.1: @dataclass(order=True) is wrong because it compares fields sequentially (amount then currency), breaking correct business logic for multi-currency comparisons.
# Task 7.2: sum() defaults its start value to integer 0, raising a type error. Using sum(items, start=Money(0, 'UZS')) solves this cleanly.

from dataclasses import dataclass
import pytest


class CurrencyMismatchError(Exception):
  pass


@dataclass(frozen=True, order=False)
class Money:
  amount: int
  currency: str

  def __add__(self, other):
    if isinstance(other, (int, float)) and other == 0:
      return self
    if not isinstance(other, Money):
      return NotImplemented
    if self.currency != other.currency:
      raise CurrencyMismatchError(
          f"Cannot add {self.currency} and {other.currency}"
      )
    return Money(self.amount + other.amount, self.currency)

  def __radd__(self, other):
    return self.__add__(other)

  def __mul__(self, factor):
    if not isinstance(factor, (int, float)):
      return NotImplemented
    return Money(int(self.amount * factor), self.currency)

  def __rmul__(self, factor):
    return self.__mul__(factor)

  def __lt__(self, other):
    if not isinstance(other, Money) or self.currency != other.currency:
      raise CurrencyMismatchError("Currency mismatch")
    return self.amount < other.amount

  def __le__(self, other):
    if not isinstance(other, Money) or self.currency != other.currency:
      raise CurrencyMismatchError("Currency mismatch")
    return self.amount <= other.amount


# Tests
def test_money_operations():
  m1 = Money(500, "UZS")
  m2 = Money(300, "UZS")

  assert m1 + m2 == Money(800, "UZS")
  assert m1 * 3 == Money(1500, "UZS")
  assert 3 * m1 == Money(1500, "UZS")
  assert sum([m1, m2], start=Money(0, "UZS")) == Money(800, "UZS")
  assert (m1 == 500) is False

  with pytest.raises(CurrencyMismatchError):
    _ = m1 + Money(100, "USD")