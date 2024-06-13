from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import Data
import pytest
import allure


class TestIngredient:

    @allure.title('Создание ингредиента с типом, именем и ценой')
    def test_create_ingredient_actual_type_name_and_price_success(self):
        ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)

        assert ingredient.type == Data.INGREDIENT_TYPE and ingredient.name == Data.INGREDIENT_NAME and ingredient.price == Data.INGREDIENT_PRICE

    @allure.title('Получение цены ингредиента через метод get_price')
    def test_get_price_success(self):
        ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)

        assert ingredient.get_price() == Data.INGREDIENT_PRICE

    @allure.title('Получение имени ингредиента через метод get_name')
    def test_get_name_success(self):
        ingredient = Ingredient(Data.INGREDIENT_TYPE, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)

        assert ingredient.get_name() == Data.INGREDIENT_NAME

    @allure.title('Получение типа ингредиента через метод get_type')
    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_success(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, Data.INGREDIENT_NAME, Data.INGREDIENT_PRICE)
        result_type = 'SAUCE' if ingredient_type == INGREDIENT_TYPE_SAUCE else 'FILLING'

        assert ingredient.get_type() == result_type
