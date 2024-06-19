from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngridient:
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'Potato',500)
        assert ingredient.get_price() == 500



    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'Potato',500)
        assert ingredient.get_name() == 'Potato'

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'Potato',500)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE