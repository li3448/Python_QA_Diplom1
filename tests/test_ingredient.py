import pytest

from helpers.generate import generate_name, generate_price, generate_ingredient
from ingredient_types import *


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_ingredient_get_type(self, ingredient_type):
        ingredient = generate_ingredient(ingredient_type=ingredient_type)

        assert ingredient.get_type() == ingredient_type

    def test_ingredient_get_name(self):
        name = generate_name()

        ingredient = generate_ingredient(name=name)

        assert ingredient.get_name() == name

    def test_ingredient_get_price(self):
        price = generate_price()

        ingredient = generate_ingredient(price=price)

        assert ingredient.get_price() == price
