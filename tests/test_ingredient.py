import pytest

from ingredient import Ingredient
from data.data import TestData


class TestIngredient:

    def test_default_ingredient_type_true(self):
        ingredient_instance = Ingredient(
            *TestData.INGREDIENTS_LIST[0].values()
        )
        assert ingredient_instance.type == TestData.INGREDIENTS_LIST[0]['type']

    def test_default_name_true(self):
        ingredient_instance = Ingredient(
            *TestData.INGREDIENTS_LIST[0].values()
        )
        assert ingredient_instance.name == TestData.INGREDIENTS_LIST[0]['name']

    def test_default_price_true(self):
        ingredient_instance = Ingredient(
            *TestData.INGREDIENTS_LIST[0].values()
        )
        assert ingredient_instance.price == TestData.INGREDIENTS_LIST[0]['price']

    def test_get_price(self):
        ingredient_instance = Ingredient(
            *TestData.INGREDIENTS_LIST[0].values()
        )
        return ingredient_instance.get_price() == TestData.INGREDIENTS_LIST[0]['price']

    def test_get_name(self):
        ingredient_instance = Ingredient(
            *TestData.INGREDIENTS_LIST[0].values()
        )
        return ingredient_instance.get_name() == TestData.INGREDIENTS_LIST[0]['name']

    @pytest.mark.parametrize(
        'ingredient',
        TestData.INGREDIENTS_LIST
    )
    def test_get_type(self, ingredient):
        ingredient_instance = Ingredient(
            *ingredient.values()
        )
        assert ingredient_instance.get_type() == ingredient['type']
