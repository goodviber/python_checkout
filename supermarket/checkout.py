from .discount_manager import DiscountManager
from collections import Counter


class Checkout:
    def __init__(self, pricing_rules=[]):
        self.discount_manager = DiscountManager(pricing_rules)
        self.rules = pricing_rules
        self.basket = []

    def scan(self, item):
        self.basket.append(item)

    def total(self):
        price = 0
        tally = Counter(self.basket)
        for item, quantity in tally.items():
            if not self.discount_manager.pricing_rules:
                price += item.price * quantity
            else:
                price += self.discount_manager.discount_price_for(
                    item, quantity)

        return self.discount_manager.discount_total(price)
