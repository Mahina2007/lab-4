# Task 10.4: Centralized string-to-class mapping at the edge (API entry point) is acceptable because it eliminates bloated if/elif branching from core business logic (Checkout).
# Task 10.5: Adding a new class requires changing exactly one place—the registry dictionary.

from abc import ABC, abstractmethod
import pytest


class PaymentMethod(ABC):

  @abstractmethod
  def fee(self, amount: int) -> int:
    pass


class CardPayment(PaymentMethod):

  def fee(self, amount: int) -> int:
    return amount * 15 // 1000


class ClickPayment(PaymentMethod):

  def fee(self, amount: int) -> int:
    return amount * 10 // 1000


class BankTransfer(PaymentMethod):

  def fee(self, amount: int) -> int:
    return 5000


class UnknownPaymentMethodError(Exception):
  pass


PAYMENT_REGISTRY = {
    "card": CardPayment,
    "click": ClickPayment,
    "bank_transfer": BankTransfer,
}


def create_payment_method(name: str) -> PaymentMethod:
  normalized = name.strip().lower()
  if normalized not in PAYMENT_REGISTRY:
    supported = ", ".join(PAYMENT_REGISTRY.keys())
    raise UnknownPaymentMethodError(
        f"Unknown method: '{name}'. Supported methods: {supported}"
    )
  return PAYMENT_REGISTRY[normalized]()


# Tests
def test_registry_normalization():
  method = create_payment_method(" CLICK ")
  assert isinstance(method, ClickPayment)


def test_registry_unknown_error():
  with pytest.raises(UnknownPaymentMethodError) as exc_info:
    create_payment_method("crypto")
  assert "crypto" in str(exc_info.value)
  assert "card" in str(exc_info.value)