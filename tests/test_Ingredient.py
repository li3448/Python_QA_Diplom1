import allure
import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    @allure.description('Стоимость ингредиента')
    @pytest.mark.parametrize('price', [' ', '1', '1.1', '     ', '123 4', 'ADV'])
    def test_get_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Potato', price)
        assert ingredient.get_price() == price

    @allure.description('Стоимость булки')
    @pytest.mark.parametrize('name', [' ', 'Bulka', 'Булка', 'QwerБу', 'Булка и вилка', 'ADV'])
    def test_get_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 500)
        assert ingredient.get_name() == name

    @allure.description('Начинка булки')
    @pytest.mark.parametrize('nachinka_or_souse', [' ', 'Майонез', 'Ketchup', 'Beef1', 'CheНасес', '!2 ВS'])
    def test_get_type(self, nachinka_or_souse):
        ingredient = Ingredient(nachinka_or_souse, 'Potato', 500)
        assert ingredient.get_type() == nachinka_or_souse
