import pytest
from supermarket.checkout import Checkout
from supermarket.item import Item
from supermarket.pricing_rule import PricingRule
from supermarket.discount_manager import DiscountManager


class TestCheckout:

    @pytest.fixture
    def pricing_rules(self):
        return [
            PricingRule.discount_rule(200, 10),
            PricingRule.multibuy_rule('A', 2, 45),
            PricingRule.multibuy_rule('B', 3, 25),
            PricingRule.percentage_discount_rule('D', 10, 10)
        ]

    @pytest.fixture
    def item_a(self):
        return Item('A', 50)

    @pytest.fixture
    def item_b(self):
        return Item('B', 30)

    @pytest.fixture
    def item_c(self):
        return Item('C', 20)

    @pytest.fixture
    def item_d(self):
        return Item('D', 10)

    def test_checkout(self):
        checkout = Checkout()
        assert checkout.basket == []
        assert checkout.total() == 0

    def test_scan(self, item_a, item_b):
        checkout = Checkout()
        checkout.scan(item_a)
        assert checkout.basket == [item_a]
        checkout.scan(item_b)
        assert checkout.basket == [item_a, item_b]

    def test_total_no_rules(self, item_a, item_b, item_c, item_d):
        checkout = Checkout()
        checkout.scan(item_a)
        checkout.scan(item_b)
        checkout.scan(item_c)
        checkout.scan(item_d)
        assert checkout.total() == 110

    def test_total_with_rules(self, item_a, item_b, item_c, item_d, pricing_rules):
        checkout = Checkout(pricing_rules)
        checkout.scan(item_a)
        checkout.scan(item_b)
        checkout.scan(item_c)
        checkout.scan(item_d)
        assert checkout.total() == 109

        checkout2 = Checkout(pricing_rules)
        checkout2.scan(item_a)
        checkout2.scan(item_b)
        checkout2.scan(item_c)
        checkout2.scan(item_c)
        checkout2.scan(item_c)
        checkout2.scan(item_c)
        checkout2.scan(item_c)
        checkout2.scan(item_c)
        checkout2.scan(item_c)
        checkout2.scan(item_c)
        checkout2.scan(item_c)
        assert checkout2.total() == 234

        checkout3 = Checkout(pricing_rules)
        checkout3.scan(item_a)
        checkout3.scan(item_a)
        checkout3.scan(item_b)
        checkout3.scan(item_b)
        checkout3.scan(item_b)
        assert checkout3.total() == 165

        checkout4 = Checkout(pricing_rules)
        checkout4.scan(item_a)
        checkout4.scan(item_a)
        checkout4.scan(item_b)
        checkout4.scan(item_b)
        checkout4.scan(item_c)
        checkout4.scan(item_c)
        checkout4.scan(item_c)
        assert checkout4.total() == 189

        checkout5 = Checkout(pricing_rules)
        checkout5.scan(item_a)
        checkout5.scan(item_a)
        checkout5.scan(item_a)
        assert checkout5.total() == 135

        checkout6 = Checkout(pricing_rules)
        checkout6.scan(item_d)
        checkout6.scan(item_d)
        checkout6.scan(item_d)
        assert checkout6.total() == 27
