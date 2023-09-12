import pytest
from supermarket.pricing_rule import PricingRule


class TestPricingRule:

    def test_discount_rule(self):
        pricing_rule = PricingRule.discount_rule(60, 10)
        assert pricing_rule.type == PricingRule.TYPE['discount']
        assert pricing_rule.apply(70) == 63
        assert pricing_rule.apply(50) == 50

    def test_multibuy_rule(self):
        pricing_rule = PricingRule.multibuy_rule('FR1', 2, 8.5)
        assert pricing_rule.type == PricingRule.TYPE['multibuy']
        assert pricing_rule.apply('FR1', 2) == 17
        assert pricing_rule.apply('FR1', 1) == None
        assert pricing_rule.apply('FR1', 3) == 25.5

    def test_percentage_discount_rule(self):
        pricing_rule = PricingRule.percentage_discount_rule('SR1', 20, 10)
        assert pricing_rule.type == PricingRule.TYPE['percentage_discount']
        assert pricing_rule.apply('SR1', 1) == 18
        assert pricing_rule.apply('SR1', 2) == 36
        assert pricing_rule.apply('SR1', 3) == 54
