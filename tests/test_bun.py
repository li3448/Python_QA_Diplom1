import pytest
from praktikum import bun
from praktikum.bun import Bun


class TestingBun(Bun):

    def __init__(self, name, price):
        super().__init__(name, price)
    def test_name_valid(self):
        bun = Bun('Супербулка', 200)
        #self.name = 'Супербулка'
        print(bun.get_name())
        assert bun.get_name() == 'Супербулка'
