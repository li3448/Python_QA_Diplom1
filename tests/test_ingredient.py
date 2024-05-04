import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *

class TestIngredient:
    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус c шипами Антарианского плоскоходца', 88, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Кристаллы марсианских альфа-сахаридов', 762, 'FILLING']
        ]
    )
    def test_get_type_successful(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient

    def test_get_price_successful(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус c шипами Антарианского плоскоходца', 88)
        assert ingredient.get_price() == 88

    def test_get_name_successful(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус c шипами Антарианского плоскоходца', 88)
        assert ingredient.get_name() == 'Соус c шипами Антарианского плоскоходца'
