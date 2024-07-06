from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_for_set_buns_method(self):
        burger = Burger()
        bun_mock = Mock()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_for_add_ingredient_method(self):
        burger = Burger()
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_for_remove_ingredient_method(self):
        burger = Burger()
        ingredient_one_mock = Mock()
        ingredient_two_mock = Mock()
        burger.add_ingredient(ingredient_one_mock)
        burger.add_ingredient(ingredient_two_mock)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == ingredient_two_mock

    def test_for_move_ingredient_method(self):
        burger = Burger()
        ingredient_one_mock = Mock()
        ingredient_two_mock = Mock()
        burger.add_ingredient(ingredient_one_mock)
        burger.add_ingredient(ingredient_two_mock)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_two_mock, ingredient_one_mock]

    def test_for_get_price_method(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_price.return_value = 988
        burger.set_buns(bun_mock)
        ingredient_one_mock = Mock()
        ingredient_one_mock.get_price.return_value = 90
        ingredient_two_mock = Mock()
        ingredient_two_mock.get_price.return_value = 1337
        burger.add_ingredient(ingredient_one_mock)
        burger.add_ingredient(ingredient_two_mock)
        exp_price = bun_mock.get_price() * 2 + ingredient_one_mock.get_price() + ingredient_two_mock.get_price()
        assert burger.get_price() == exp_price
