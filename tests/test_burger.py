import pytest

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from unittest.mock import Mock


class TestBurger:
    def test_set_bun(self):
        my_burger = Burger()
        my_bun = Bun('bulka', 200)
        my_burger.set_buns(my_bun)
        assert my_burger.bun == my_bun

    def test_add_ingredient(self):
        my_burger = Burger()
        my_ing_1 = Ingredient('sauce', 'tomato', 50)
        my_ing_2 = Ingredient('filling', 'fish', 250)
        my_burger.add_ingredient(my_ing_1)
        my_burger.add_ingredient(my_ing_2)
        assert len(my_burger.ingredients) == 2

    def test_remove_ingredient(self):
        my_burger = Burger()
        my_ing_1 = Ingredient('sauce', 'tomato', 50)
        my_ing_2 = Ingredient('filling', 'fish', 250)
        my_ing_3 = Ingredient('sauce', 'beshamel', 60)
        my_burger.add_ingredient(my_ing_1)
        my_burger.add_ingredient(my_ing_2)
        my_burger.add_ingredient(my_ing_3)
        my_burger.remove_ingredient(0)
        assert my_burger.ingredients[0] == my_ing_2

    def test_move_ingredient(self):
        my_burger = Burger()
        my_ing_1 = Ingredient('sauce', 'tomato', 50)
        my_ing_2 = Ingredient('filling', 'fish', 250)
        my_burger.add_ingredient(my_ing_1)
        my_burger.add_ingredient(my_ing_2)
        my_burger.move_ingredient(0, 1)
        assert my_burger.ingredients[0] == my_ing_2

    def test_get_price(self):
        my_burger = Burger()
        my_bun = Bun('bulka', 200)
        my_burger.set_buns(my_bun)
        my_ing_1 = Ingredient('sauce', 'tomato', 50)
        my_ing_2 = Ingredient('filling', 'fish', 250)
        my_burger.add_ingredient(my_ing_1)
        my_burger.add_ingredient(my_ing_2)
        assert my_burger.get_price() == 700

    @pytest.mark.parametrize('part', ['bulka', 'sauce', 'tomato', 'filling', 'fish', 'Price', '1100'])
    def test_get_receipt(self, part):
        mock_bun = Mock()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        mock_bun.get_name.return_value = 'bulka'
        mock_bun.get_price.return_value = 400
        mock_ing_1.get_type.return_value = 'sauce'
        mock_ing_1.get_name.return_value = 'tomato'
        mock_ing_1.get_price.return_value = 50
        mock_ing_2.get_type.return_value = 'filling'
        mock_ing_2.get_name.return_value = 'fish'
        mock_ing_2.get_price.return_value = 250

        my_burger = Burger()
        my_burger.set_buns(mock_bun)
        my_burger.add_ingredient(mock_ing_1)
        my_burger.add_ingredient(mock_ing_2)
        my_burger.get_price()
        assert part in my_burger.get_receipt()

    def test_constructor_burger_bun(self):
        my_burger = Burger()
        my_bun = Bun('bulka', 400)
        my_burger.set_buns(my_bun)
        assert my_burger.bun != None

    def test_constructor_burger_ing(self):
        my_burger = Burger()
        my_ing_1 = Ingredient('sauce', 'tomato', 50)
        my_ing_2 = Ingredient('filling', 'fish', 250)
        my_burger.add_ingredient(my_ing_1)
        my_burger.add_ingredient(my_ing_2)
        assert len(my_burger.ingredients) == 2
