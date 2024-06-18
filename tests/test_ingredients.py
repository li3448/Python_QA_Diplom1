import allure
import pytest

from ingredient import Ingredient
from data import BurgerConsist as bc

class TestIngredient:
    @allure.title('проверка сборки бургера с пустым и незаданным типом ингредиента')
    @pytest.mark.parametrize('ingredient_type', ['', None])
    def test_none_and_empty_ingredient_type(self, ingredient_type):
            sauce = Ingredient(ingredient_type, bc.INGREDIENT_TYPE_SAUCE_NAME, bc.SAUCE_PRICE)
            assert sauce.type == ingredient_type


    @allure.title('проверка сборки бургера с пустым и незаданным именем ингредиента')
    @pytest.mark.parametrize('name', ['', None])
    def test_none_and_empty_ingredient_name(self, name):
            sauce = Ingredient(bc.INGREDIENT_TYPE_SAUCE, name, bc.SAUCE_PRICE)
            assert sauce.name == name

    @allure.title('проверка сборки бургера с пустой и незаданной ценой ингредиента')
    @pytest.mark.parametrize('price', ['', None])
    def test_none_and_empty_ingredient_price(self, price):
            sauce = Ingredient(bc.INGREDIENT_TYPE_SAUCE, bc.INGREDIENT_TYPE_FILLING_NAME, price)
            assert sauce.price == price


# тест для метода get_price
    @allure.title('проверка получения стоимости ингредиента')
    def test_get_price(self):
            sauce = Ingredient(bc.INGREDIENT_TYPE_SAUCE, bc.INGREDIENT_TYPE_SAUCE_NAME, bc.SAUCE_PRICE)
            assert sauce.get_price() == bc.SAUCE_PRICE

# тест для метода get_name
    @allure.title('проверка получения  имени ингредиента')
    def test_get_name(self):
            sauce = Ingredient(bc.INGREDIENT_TYPE_SAUCE, bc.INGREDIENT_TYPE_SAUCE_NAME, bc.SAUCE_PRICE)
            assert sauce.get_name() == bc.INGREDIENT_TYPE_SAUCE_NAME

# тест для метода get_type
    @allure.title('проверка получения  типа ингредиента')
    def test_get_type(self):
            sauce = Ingredient(bc.INGREDIENT_TYPE_SAUCE, bc.INGREDIENT_TYPE_SAUCE_NAME, bc.SAUCE_PRICE)
            assert sauce.get_type() == bc.INGREDIENT_TYPE_SAUCE



