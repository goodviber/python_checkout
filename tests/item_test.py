import pytest
from supermarket.item import Item


class TestItem:

    @pytest.fixture
    def item(self):
        return Item('FR1', 10)

    def test_item(self, item):
        assert item.code == 'FR1'
        assert item.price == 10

    def test_item_invalid_code(self, item):
        with pytest.raises(ValueError):
            Item('', 10)

    def test_item_invalid_price(self, item):
        with pytest.raises(ValueError):
            Item('FR1', -10)
