import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    @pytest.mark.parametrize("number, name_bun, price_bun", [[0, "black bun", 100], [1, "white bun", 200],
                                                             [2, "red bun", 300]])
    def test_database_bun_success(self, number, name_bun, price_bun):
        database = Database()
        assert database.buns[number].name == name_bun and database.buns[number].price == price_bun

    @pytest.mark.parametrize("number, type_ingr, name_ingr, price_ingr", [[0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
                                                                          [1, INGREDIENT_TYPE_SAUCE, "sour cream", 200],
                                                                          [2, INGREDIENT_TYPE_SAUCE, "chili sauce",
                                                                           300],
                                                                          [3, INGREDIENT_TYPE_FILLING, "cutlet", 100],
                                                                          [4, INGREDIENT_TYPE_FILLING, "dinosaur", 200],
                                                                          [5, INGREDIENT_TYPE_FILLING, "sausage", 300]])
    def test_database_ingredient_success(self, number, type_ingr, name_ingr, price_ingr):
        database = Database()
        assert (database.ingredients[number].name == name_ingr and database.ingredients[number].price == price_ingr and
                database.ingredients[number].type == type_ingr)

    def test_available_buns_success(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients_success(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
