from supermarket.pricing_rule import PricingRule


class DiscountManager:
    def __init__(self, pricing_rules=[]):
        self.pricing_rules = pricing_rules

    @property
    def pricing_rules(self):
        return self._pricing_rules

    @pricing_rules.setter
    def pricing_rules(self, value):
        if not isinstance(value, list):
            raise ValueError('Pricing rules must be a list')
        self._pricing_rules = value

    def discount_price_for(self, item, quantity):
        discount_price = 0
        for rule in self.pricing_rules:
            if not rule.type == PricingRule.TYPE['discount']:
                discount_price += rule.apply(item.code, quantity) or 0
            if not discount_price == 0:
                return discount_price
        return item.price * quantity

    def discount_total(self, total):
        for rule in self.pricing_rules:
            if rule.type == PricingRule.TYPE['discount']:
                total = rule.apply(total)
        return total
