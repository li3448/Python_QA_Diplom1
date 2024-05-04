from praktikum.database import Database
from praktikum.ingredient_types import *

class TestDatabase:

    def test_ingredients_available(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(database.available_ingredients()) == 6
        assert all([i.get_type() == INGREDIENT_TYPE_SAUCE for i in ingredients[:3]])
        assert all([i.get_type() == INGREDIENT_TYPE_FILLING for i in ingredients[3:]])
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[1].get_price() == 200
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[2].get_price() == 300
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[4].get_price() == 200
        assert ingredients[5].get_name() == "sausage"
        assert ingredients[5].get_price() == 300
    def test_buns_available(self):
        database = Database()
        buns = database.available_buns()
        assert len(database.available_buns()) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200
        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300
