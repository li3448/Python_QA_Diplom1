from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDatabase:
    def test_for_available_buns_method(self):
        database = Database()
        buns_available = database.available_buns()

        assert buns_available[1].get_name() == "white bun" and buns_available[1].get_price() == 200

    def test_for_available_ingredients_method(self):
        database = Database()
        ingredients_available = database.available_ingredients()

        assert ingredients_available[1].get_type() == INGREDIENT_TYPE_SAUCE and ingredients_available[
            1].get_name() == "sour cream" and ingredients_available[1].get_price() == 200
