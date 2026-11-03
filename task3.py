# Task 3.1: FamilySubscription.__init__ missed calling super().__init__(user, months). The error appears when price() runs because members attribute is missing or base initialization failed when calculating net price.
# Task 3.4: Only the VAT_PERCENT constant in the base Subscription class needed to be changed.

class Subscription:
  VAT_PERCENT = 12

  def __init__(self, user, months):
    self.user = user
    self.months = months
    self.base_monthly = 50_000

  def net(self):
    return self.base_monthly * self.months

  def price(self):
    net_price = self.net()
    return net_price * (100 + self.VAT_PERCENT) // 100


class StudentSubscription(Subscription):

  def net(self):
    return super().net() // 2


class FamilySubscription(Subscription):

  def __init__(self, user, months, members):
    super().__init__(user, months)
    self.members = members

  def net(self):
    extra = 20_000 * (len(self.members) - 1) * self.months
    return super().net() + extra


# Tests
def test_standard_subscription():
  sub = Subscription("Ali", 3)
  # 50,000 * 3 = 150,000 net -> + 12% VAT = 168,000
  assert sub.price() == 168_000


def test_student_subscription():
  sub = StudentSubscription("Vali", 3)
  # (150,000 // 2) = 75,000 net -> + 12% VAT = 84,000
  assert sub.price() == 84_000


def test_family_subscription():
  sub = FamilySubscription("Gani", 3, members=[1, 2, 3, 4])
  # Extra: 20,000 * (4 - 1) * 3 = 180,000. Total net = 150,000 + 180,000 = 330,000
  # + 12% VAT = 369,600
  assert sub.price() == 369_600