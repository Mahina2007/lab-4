from functools import partial

# --- Style 1: Classes ---
class PercentageDiscount:
    def __init__(self, percent):
        self.percent = percent
    def apply(self, total):
        return total * (100 - self.percent) // 100

class FixedDiscount:
    def __init__(self, amount):
        self.amount = amount
    def apply(self, total):
        return max(0, total - self.amount)

# --- Style 2: Plain functions / partials ---
def percentage_discount(total, percent):
    return total * (100 - percent) // 100

def fixed_discount(total, amount):
    return max(0, total - amount)

def free_delivery(total, threshold, delivery_fee):
    # Notice: Free delivery depends on order total, but what if it needs item weight/address?
    return total  # Does NOT strictly fit apply(total) -> int without extra context!