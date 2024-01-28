import pytest

from tests.data import TestData
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """
    Тесты создание объекта класса Ingredient
    """
    """Тест проверка типа ингредиента для бургера"""

    @pytest.mark.parametrize(
        "types", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_types_of_ingredient(self, types):
        ingredient = Ingredient(types, TestData.INGREDIENT_NAME,
                                TestData.INGREDIENT_PRICE)
        assert ingredient.type == types, f"Ожидалась ингредиент {types}, получен {ingredient.type}"

    """Тест проверка типа данных вид ингредиента для бургера - str"""
    def test_types_of_ingredient_is_str(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME,
                                TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.type, str), f"Ожидалась 'str', но получено {type(ingredient.type)}"

    """Тест проверка имени ингредиента для бургера"""
    @pytest.mark.parametrize(
        "name", ["Имя", "Имя1", "имя", "name", "", None])
    def test_name_of_ingredient(self, name):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, name,
                                TestData.INGREDIENT_PRICE)
        assert ingredient.name == name, f"Ожидалась ингредиент {name}, получен {ingredient.name}"

    """Тест проверка типа данных имени ингредиента для бургера - str"""
    def test_name_of_ingredient_is_str(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME,
                                TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.name, str), f"Ожидалась 'str', но получено {type(ingredient.name)}"

    """Тест проверка цены ингредиента для бургера"""
    @pytest.mark.parametrize(
        "price", [120.7, 120, 120000000000000, 0, -1])
    def test_prices_of_ingredient(self, price):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME,
                                price)
        assert ingredient.price == price, f"Ожидалась цена {price}, получен {ingredient.price}"

    """Тест проверка типа данных цены ингредиента для бургера - float"""
    def test_price_of_ingredient_is_float(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME,
                                TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.price, float), f"Ожидалась 'float', но получено {type(ingredient.price)}"

    """
    Тесты методов класса Ingredient
    """
    """Проверка успешное получение типа ингредиента для бургера методом get_type"""

    @pytest.mark.parametrize(
        "types", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_true_type(self, types):
        ingredient = Ingredient(types, TestData.INGREDIENT_NAME,
                                TestData.INGREDIENT_PRICE)
        assert ingredient.get_type() == types, f"Ожидалась тип ингредиента {types}, получен {ingredient.get_type()}"

    """Проверка метод get_type на возвращаемый тип данных - str"""
    def test_get_type_true_return_str(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME,
                                TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.get_type(), str), f"Ожидалась 'str', но получено {type(ingredient.get_type())}"

    """Проверка успешное получение имени ингредиента для бургера методом get_name"""
    @pytest.mark.parametrize(
        "name", ["Имя", "Имя1", "имя", "name", "", None])
    def test_get_name_true_name(self, name):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, name,
                                TestData.INGREDIENT_PRICE)
        assert ingredient.get_name() == name, f"Ожидалась имя ингредиента {name}, получен {ingredient.get_name()}"

    """Проверка метод get_name на возвращаемый тип данных - str"""
    def test_get_name_return_is_str(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME,
                                TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.get_name(), str), f"Ожидалась 'str', но получено {type(ingredient.get_name())}"

    """Проверка успешное получение цены ингредиента для бургера методом get_name"""
    @pytest.mark.parametrize(
        "price", [120.7, 120, 120000000000000, 0, -1])
    def test_get_price_true_price(self, price):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME,
                                price)
        assert ingredient.get_price() == price, f"Ожидалась имя ингредиента {price}, получен {ingredient.get_price()}"

    """Проверка метод get_name на возвращаемый тип данных - float"""
    def test_get_price_return_is_float(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME,
                                TestData.INGREDIENT_PRICE)
        assert isinstance(ingredient.get_price(), float), f"Ожидалась 'float', но получено {type(ingredient.get_price())}"