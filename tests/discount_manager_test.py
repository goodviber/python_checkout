import pytest
from supermarket.discount_manager import DiscountManager
from supermarket.pricing_rule import PricingRule
from supermarket.item import Item


class TestDiscountManager:

    @pytest.fixture
    def pricing_rules(self):
        return [
            PricingRule.discount_rule(60, 10),
            PricingRule.multibuy_rule('FR1', 2, 8.5),
            PricingRule.percentage_discount_rule('SR1', 20, 10)
        ]

    @pytest.fixture
    def item(self):
        return Item('FR1', 10)

    @pytest.fixture
    def item2(self):
        return Item('SR1', 20)

    def test_discount_manager(self):
        discount_manager = DiscountManager()
        assert discount_manager.pricing_rules == []

    def test_discount_price_for(self, item, item2, pricing_rules):
        no_rules = DiscountManager()
        assert no_rules.discount_price_for(item, 2) == 20
        assert no_rules.discount_price_for(item2, 1) == 20

        with_rules = DiscountManager(pricing_rules)
        assert with_rules.discount_price_for(item, 2) == 17
        assert with_rules.discount_price_for(item2, 1) == 18

    def test_discount_total(self, pricing_rules):
        discount_manager = DiscountManager(pricing_rules)
        assert discount_manager.discount_total(100) == 90
        assert discount_manager.discount_total(50) == 50
