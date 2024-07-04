from conftest import mok_bun, mok_ingredient, mock_ingredients, burger
from praktikum.burger import Burger


def test_set_buns(burger, mok_bun):
    burger = Burger()
    burger.set_buns(mok_bun)
    assert mok_bun == burger.bun


def test_add_ingredient(burger, mok_ingredient):
    burger.add_ingredient(mok_ingredient)
    assert mok_ingredient in burger.ingredients


def test_remove_ingredient(burger, mok_ingredient):
    burger.add_ingredient(mok_ingredient)
    burger.remove_ingredient(0)
    assert mok_ingredient not in burger.ingredients


def test_move_ingredient(mok_ingredient, mock_ingredients, burger):
    burger = Burger()
    burger.add_ingredient(mok_ingredient)
    index = burger.ingredients.index(mok_ingredient)
    burger.move_ingredient(0, 3)
    assert burger.ingredients[0] == mok_ingredient
