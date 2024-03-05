import pytest
import praktikum.ingredient_types

from praktikum.ingredient import Ingredient

""" Тесты для класса Ingredient """
class TestIngredient:
    """ Тест для проверки инициализации объекта Ingredient """
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE, "mayonnaise", 50.0),
        (praktikum.ingredient_types.INGREDIENT_TYPE_FILLING, "cheese", 100.0),
        (praktikum.ingredient_types.INGREDIENT_TYPE_FILLING, "ham", 150.0)
    ])
    def test_init(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        # Проверяем, что getter'ы возвращают правильные значения
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    """ Тест для проверки метода get_price() """
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE, "ketchup", 40.0),
        (praktikum.ingredient_types.INGREDIENT_TYPE_FILLING, "tomato", 80.0),
        (praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE, "mustard", 30.0)
    ])
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        # Проверяем, что полученная цена совпадает с ожидаемой
        assert ingredient.get_price() == price

    """ Тест для проверки метода get_name() """
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE, "mayonnaise", 50.0),
        (praktikum.ingredient_types.INGREDIENT_TYPE_FILLING, "cheese", 100.0),
        (praktikum.ingredient_types.INGREDIENT_TYPE_FILLING, "ham", 150.0)
    ])
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        # Проверяем, что полученное название совпадает с ожидаемым
        assert ingredient.get_name() == name

    """ Тест для проверки метода get_type() """
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE, "ketchup", 40.0),
        (praktikum.ingredient_types.INGREDIENT_TYPE_FILLING, "tomato", 80.0),
        (praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE, "mustard", 30.0)
    ])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        # Проверяем, что полученный тип совпадает с ожидаемым
        assert ingredient.get_type() == ingredient_type
