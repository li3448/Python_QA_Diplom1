from data import *
import pytest
import allure
from practicum.ingredient import Ingredient


class TestIngredient:

    @allure.title('Проверяем получение цены')
    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', [
        [BurgerData.ingredient_type_filling, BurgerData.ingredient_name_filling, BurgerData.ingredient_price_filling],
        [BurgerData.ingredient_type_sauce, BurgerData.ingredient_name_sauce, BurgerData.ingredient_price_sauce]
    ])
    def test_get_price(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_price() == ingredient_price

    @allure.title('Проверяем получение имени ингредиента')
    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', [
        [BurgerData.ingredient_type_filling, BurgerData.ingredient_name_filling, BurgerData.ingredient_price_filling],
        [BurgerData.ingredient_type_sauce, BurgerData.ingredient_name_sauce, BurgerData.ingredient_price_sauce]
    ])
    def test_get_name(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_name() == ingredient_name

    @allure.title('Проверяем получение цены')
    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price', [
        [BurgerData.ingredient_type_filling, BurgerData.ingredient_name_filling, BurgerData.ingredient_price_filling],
        [BurgerData.ingredient_type_sauce, BurgerData.ingredient_name_sauce, BurgerData.ingredient_price_sauce]
    ])
    def test_get_type(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_type() == ingredient_type
