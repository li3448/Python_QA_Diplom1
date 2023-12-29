from praktikum.ingredient import Ingredient
from data import HelpData
import pytest

class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', HelpData.ingredients_data)
    def test_get_type_create_new_ingredient_check_type(self, ingredient_type, name, price):
        new_ingredient = Ingredient(ingredient_type, name, price)
        assert new_ingredient.get_type() == ingredient_type

    def test_get_name_create_new_ingredient_check_name(self):
        new_ingredient = Ingredient('salad', 'romano', 0.4)
        assert new_ingredient.get_name() == 'romano'

    def test_get_price_create_new_ingredient_check_price(self):
        new_ingredient = Ingredient('salad', 'romano', 0.4)
        assert new_ingredient.get_price() == 0.4