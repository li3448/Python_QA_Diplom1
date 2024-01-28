from praktikum.ingredient import Ingredient
from praktikum import ingredient_types
from data import TestData
import pytest


class TestIngredient:

    @pytest.mark.parametrize('price',
                             [TestData.BUN_PRICE_VALID, TestData.BUN_PRICE_FLOAT, TestData.BUN_PRICE_LESS_THAN_ZERO])
    def test_get_price_successful(self, price):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, TestData.SAUCE_NAME_CHILI, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_name',
                             [TestData.SAUCE_NAME_CHILI, TestData.SAUCE_NAME_HOT, TestData.SAUCE_NAME_SOUR])
    def test_get_name_of_sauce_successful(self, ingredient_name):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, ingredient_name, TestData.BUN_PRICE_VALID)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize('ingredient_name',
                             [TestData.FILLING_NAME_SAUSAGE, TestData.FILLING_NAME_DINOSAUR,
                              TestData.FILLING_NAME_CUTLET])
    def test_get_name_of_filling_successful(self, ingredient_name):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, ingredient_name, TestData.BUN_PRICE_VALID)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize('ingredient_type',
                             [ingredient_types.INGREDIENT_TYPE_SAUCE, ingredient_types.INGREDIENT_TYPE_FILLING])
    def test_get_type_successful(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, TestData.SAUCE_NAME_CHILI, TestData.BUN_PRICE_VALID)
        assert ingredient.get_type() == ingredient_type
