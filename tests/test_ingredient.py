import pytest

from helpers.generate import generate_name, generate_price
from ingredient import Ingredient
from ingredient_types import *


@pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
def test_ingredient_get_type_name_price(ingredient_type):
    name = generate_name()
    price = generate_price()

    ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)

    assert (ingredient.get_type() == ingredient_type and ingredient.get_name() == name
            and ingredient.get_price() == price)
