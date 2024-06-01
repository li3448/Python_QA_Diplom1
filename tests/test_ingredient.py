import pytest

from praktikum import ingredient_types
from data import Data


class TestIngredient:
    def test_get_name_ingredient_return_name_ingredient(self, ingredient_instance):
        assert ingredient_instance.get_name() == Data.BUN_NAME

    def test_get_price_ingredient_return_price_ingredient(self, ingredient_instance):
        assert ingredient_instance.get_price() == Data.BUN_PRICE

    @pytest.mark.parametrize('ingredient', [ingredient_types.INGREDIENT_TYPE_FILLING,
                                            ingredient_types.INGREDIENT_TYPE_SAUCE])
    def test_get_price_ingredient_return_type_ingredient(self, ingredient_instance, ingredient):
        ingredient_instance.type = ingredient
        assert ingredient_instance.get_type() == ingredient
