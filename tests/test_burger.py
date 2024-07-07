import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import patch

def test_burger_set_buns():
    bun = Bun("test_bun", 50)
    burger = Burger()
    burger.set_buns(bun)
    assert burger.bun == bun

def test_burger_add_ingredient():
    ingredient = Ingredient("FILLING", "test_filling", 30)
    burger = Burger()
    burger.add_ingredient(ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ingredient

def test_burger_remove_ingredient():
    ingredient = Ingredient("FILLING", "test_filling", 30)
    burger = Burger()
    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0

def test_burger_move_ingredient():
    ingredient1 = Ingredient("FILLING", "test_filling1", 30)
    ingredient2 = Ingredient("FILLING", "test_filling2", 40)
    burger = Burger()
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == ingredient2
    assert burger.ingredients[1] == ingredient1

def test_burger_get_price():
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 50
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 30
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    assert burger.get_price() == 130


def test_burger_get_receipt():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "test_bun"
    bun.get_price.return_value = 50
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "test_filling"
    ingredient.get_type.return_value = "FILLING"
    ingredient.get_price.return_value = 30

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    receipt_lines = burger.get_receipt().split('\n')
    assert receipt_lines[0] == '(==== test_bun ====)'
    assert receipt_lines[1] == '= filling test_filling ='
    assert receipt_lines[2] == '(==== test_bun ====)'
    assert receipt_lines[4] == 'Price: 130'


# @pytest.mark.parametrize("bun_price, ingredient_prices, total_price", [
#     (50, [30], 130),
#     (100, [], 200),
#     (70, [20, 30], 190)
# ])
# def test_burger_get_receipt(bun_price, ingredient_prices, total_price):
#     # Mock for Bun
#     bun = Mock(spec=Bun)
#     bun.get_name.return_value = "test_bun"
#     bun.get_price.return_value = bun_price
#
#     # Create burger
#     burger = Burger()
#     burger.set_buns(bun)
#
#     # Add ingredients
#     for price in ingredient_prices:
#         ingredient = Mock(spec=Ingredient)
#         ingredient.get_name.return_value = "test_filling"
#         ingredient.get_type.return_value = "FILLING"
#         ingredient.get_price.return_value = price
#         burger.add_ingredient(ingredient)
#
#     receipt = burger.get_receipt()
#     print(f"Receipt:\n{receipt}")  # Debug print
#     receipt_lines = receipt.split('\n')
#
#     assert receipt_lines[0] == '(==== test_bun ====)'
#     assert all(
#         receipt_lines[i+1] == f'= filling test_filling =' for i in range(len(ingredient_prices))
#     )
#     assert receipt_lines[len(ingredient_prices) + 1] == f'(==== test_bun ====)'
#     assert receipt_lines[len(ingredient_prices) + 2] == f'Price: {total_price}'