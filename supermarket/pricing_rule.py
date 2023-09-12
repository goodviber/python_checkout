class PricingRule:

    TYPE = {'discount': 1, 'multibuy': 2, 'percentage_discount': 3}

    def __init__(self, type, func):
        self.type = type
        self.func = func

    def apply(self, *args):
        return self.func(*args)

    @classmethod
    def discount_rule(self, minimum_spend, percentage_discount):
        def rule(total):
            if total >= minimum_spend:
                return total * (1 - percentage_discount / 100)
            return total

        return PricingRule(PricingRule.TYPE['discount'], rule)

    @classmethod
    def multibuy_rule(self, item_code, qualifying_quantity, discount_price):
        def rule(code, quantity):
            if code == item_code and quantity >= qualifying_quantity:
                return discount_price * quantity

        return PricingRule(PricingRule.TYPE['multibuy'], rule)

    @classmethod
    def percentage_discount_rule(self, item_code, item_price, percentage_discount):
        def rule(code, quantity):
            if code == item_code:
                return (item_price * (1 - percentage_discount / 100)) * quantity

        return PricingRule(PricingRule.TYPE['percentage_discount'], rule)
