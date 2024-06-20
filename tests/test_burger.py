import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_create_burger_true(self):
        burger = Burger()

        assert burger.bun is None and burger.ingredients == []

    def test_set_buns_true(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.name = 'Булка Ньютона'
        mock_bun.price = 2.5
        burger.set_buns(mock_bun)

        assert burger.bun.name == 'Булка Ньютона' and burger.bun.price == 2.5

    @pytest.mark.parametrize('type_ingredient', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_add_ingredient_true(self, type_ingredient):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.type = type_ingredient
        mock_ingredient.name = 'Космический Раф'
        mock_ingredient.price = 5.0
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients

    @pytest.mark.parametrize('type_ingredient', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_remove_ingredient_true(self, type_ingredient):
        burger = Burger()
        ingredient = Ingredient(type_ingredient, 'Космический Раф', 5.0)
        burger.add_ingredient(ingredient)
        index_ingredient = burger.ingredients.index(ingredient)
        burger.remove_ingredient(index_ingredient)

        assert burger.ingredients == []

    @pytest.mark.parametrize('type_ingredient', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_move_ingredient_true(self, type_ingredient):
        burger = Burger()
        ingredient_one = Ingredient(type_ingredient, 'Космический Раф', 5.0)
        ingredient_two = Ingredient(type_ingredient, 'Золотой Раф', 10.0)
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        burger.move_ingredient(0, 1)

        assert burger.ingredients.index(ingredient_one) == 1

    @pytest.mark.parametrize('type_ingredient', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_price_true(self, type_ingredient):
        burger = Burger()
        bun = Bun('Булка Ньютона', 2.5)
        ingredient_one = Ingredient(type_ingredient, 'Космический Раф', 5.0)
        ingredient_two = Ingredient(type_ingredient, 'Золотой Раф', 10.0)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)

        assert burger.get_price() == 20.0

    @pytest.mark.parametrize('type_ingredient', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_receipt_true(self, type_ingredient):
        burger = Burger()
        bun = Bun('Булка Ньютона', 2.5)
        ingredient_one = Ingredient(type_ingredient, 'Космический Раф', 5.0)
        ingredient_two = Ingredient(type_ingredient, 'Золотой Раф', 10.0)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)

        assert burger.bun.name in burger.get_receipt()
