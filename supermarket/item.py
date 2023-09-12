class Item:
    def __init__(self, code, price):
        self.code = code
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self._price = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        if not value:
            raise ValueError('Code cannot be empty')
        self._code = value

    def __str__(self):
        return f'{self.code}: {self.price}'

    def __repr__(self):
        return f'{self.code}: {self.price}'
