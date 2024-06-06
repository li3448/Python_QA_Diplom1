from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import Helpers


class TestBurger:

    def test_set_buns(self):  #Проверка добавления булки в бургер

        mock_bun = Mock()
        mock_bun.bun = Bun(Helpers.MOCK_BUN_NAME, Helpers.MOCK_BUN_PRICE)
        burger = Burger()

        burger.set_buns(mock_bun.bun)

        assert burger.bun.get_name() == Helpers.MOCK_BUN_NAME

    def test_check_price(self):  # Проверка цены бургера

        mock_bun = Mock()
        mock_bun.bun = Bun(Helpers.MOCK_BUN_NAME, Helpers.MOCK_BUN_PRICE)
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient(Helpers.MOCK_INGREDIENT_TYPE, Helpers.MOCK_INGREDIENT_NAME, Helpers.MOCK_INGREDIENT_PRICE)
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        burger.add_ingredient(mock_ingredient.ingredients)

        assert burger.get_price() == 4010
    def test_add_ingredient(self):   #Проверка добавления ингридиентов

        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient(Helpers.MOCK_INGREDIENT_TYPE, Helpers.MOCK_INGREDIENT_NAME, Helpers.MOCK_INGREDIENT_PRICE)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredients)
        assert len(burger.ingredients) == 1

    def test_delete_ingredient(self): #Проверка удаления ингредиентов из бургера
        mock_ingredient = Mock()
        mock_ingredient.ingredients = Ingredient(Helpers.MOCK_INGREDIENT_TYPE, Helpers.MOCK_INGREDIENT_NAME, Helpers.MOCK_INGREDIENT_PRICE)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredients)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_relocate_ingredient(self): #Проверка перемещения ингредиентов
        mock_ingredient = Mock()
        mock_ingredient.ingredients_1 = Ingredient(Helpers.MOCK_INGREDIENT_TYPE, Helpers.MOCK_INGREDIENT_NAME, Helpers.MOCK_INGREDIENT_PRICE)
        mock_ingredient.ingredients_2 = Ingredient(Helpers.INGREDIENT_TYPE, Helpers.INGREDIENT_NAME, Helpers.INGREDIENT_PRICE)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredients_2)
        burger.add_ingredient(mock_ingredient.ingredients_1)
        burger.move_ingredient(0, 1)

        assert burger.ingredients.index(mock_ingredient.ingredients_1) == 0


