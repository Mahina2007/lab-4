from abc import ABC, abstractmethod


class PaymentMethod(ABC):

  @abstractmethod
  def fee(self, amount: int) -> int:
    pass

  @property
  @abstractmethod
  def refundable(self) -> bool:
    pass


class CardPayment(PaymentMethod):

  def fee(self, amount: int) -> int:
    return amount * 15 // 1000

  @property
  def refundable(self) -> bool:
    return True


class ClickPayment(PaymentMethod):

  def fee(self, amount: int) -> int:
    return amount * 10 // 1000

  @property
  def refundable(self) -> bool:
    return True


class PaymePayment(PaymentMethod):

  def fee(self, amount: int) -> int:
    return amount * 10 // 1000

  @property
  def refundable(self) -> bool:
    return True


class CashPayment(PaymentMethod):

  def fee(self, amount: int) -> int:
    return 0

  @property
  def refundable(self) -> bool:
    return False


class BankTransfer(PaymentMethod):

  def fee(self, amount: int) -> int:
    return 5000

  @property
  def refundable(self) -> bool:
    return True


class Checkout:

  def pay(self, method: PaymentMethod, amount: int):
    fee = method.fee(amount)
    return {"charged": amount + fee, "refundable": method.refundable}


# Tests
def test_checkout_card():
  checkout = Checkout()
  res = checkout.pay(CardPayment(), 100_000)
  assert res == {"charged": 101_500, "refundable": True}


def test_checkout_cash():
  checkout = Checkout()
  res = checkout.pay(CashPayment(), 100_000)
  assert res == {"charged": 100_000, "refundable": False}


def test_bank_transfer():
  checkout = Checkout()
  res = checkout.pay(BankTransfer(), 100_000)
  assert res == {"charged": 105_000, "refundable": True}