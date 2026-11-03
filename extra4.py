class NoLoyalty:
    def discount_percent(self):
        return 0

    def points_for(self, amount):
        return 0

class Customer:
    def __init__(self, name, loyalty=None):
        self.name = name
        # Customer or factory ensures loyalty is never None
        self.loyalty = loyalty if loyalty is not None else NoLoyalty()

def checkout_summary(customer, amount):
    # Completely free of None checks!
    discount = amount * customer.loyalty.discount_percent() // 100
    points = customer.loyalty.points_for(amount)
    return discount, points
