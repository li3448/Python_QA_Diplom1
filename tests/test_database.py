import pytest
from praktikum.database import Database


class TestDatabase:

    def test_available_buns(self):
        data = Database()

        assert len(data.available_buns()) == 3

    def test_available_ingredients(self):
        data = Database()

        assert len(data.available_ingredients()) == 6

    @pytest.mark.parametrize("bun, price", [["black bun", 100.00],
                                            ["white bun", 200.00],
                                            ["red bun", 300.00]])
    def test_available_buns_lst(self, bun: str, price: float):
        data = Database()
        data.buns = (bun, price)

        assert data.available_buns() == data.buns

    @pytest.mark.parametrize("type_ingredient, ingredient, price", [["filling", "cutlet", 100.00],
                                                                    ["sauce",  "hot sauce", 100.00],
                                                                    ["filling", "sausage", 300.00]])
    def test_available_ingredients_lst(self, type_ingredient, ingredient, price):
        data = Database()
        data.ingredients = (type_ingredient, ingredient, price)

        assert data.available_ingredients() == data.ingredients



