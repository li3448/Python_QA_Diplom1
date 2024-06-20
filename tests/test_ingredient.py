import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize('type_ingredient', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_type_name_price_ingredient_true(self, type_ingredient):
        ingredient = Ingredient(type_ingredient, 'Космический Раф', 5.0)

        assert ingredient.type == ingredient.type and ingredient.name == 'Космический Раф' and ingredient.price == 5.0

    @pytest.mark.parametrize('type_ingredient', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_ingredient_true(self, type_ingredient):
        ingredient = Ingredient(type_ingredient, 'Космический Раф', 5.0)

        assert ingredient.get_type() == ingredient.type

    @pytest.mark.parametrize('type_ingredient', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_name_ingredient_true(self, type_ingredient):
        ingredient = Ingredient(type_ingredient, 'Космический Раф', 5.0)

        assert ingredient.get_name() == 'Космический Раф'

    @pytest.mark.parametrize('type_ingredient', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_price_ingredient_true(self, type_ingredient):
        ingredient = Ingredient(type_ingredient, 'Космический Раф', 5.0)

        assert ingredient.get_price() == 5.0
