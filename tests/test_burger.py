from unittest.mock import Mock, patch

from burger import Burger
from database import Database
from test_data.test_data import TestData


class TestBurger:

    def test_default_bun_none_true(self):
        burger = Burger()
        assert burger.bun == None

    def test_default_ingredients_empty_list_true(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        burger.set_buns(TestData.BUN)
        assert burger.bun == TestData.BUN

    def test_set_another_buns_true(self):
        burger = Burger()
        burger.set_buns(TestData.BUN)
        burger.set_buns(TestData.ANOTHER_BUN)
        assert burger.bun == TestData.ANOTHER_BUN

    def test_add_ingredient_success(self):
        burger = Burger()
        ingredient_mock = Mock(**TestData.INGREDIENTS_LIST[1])
        # ingredient_mock.name = TestData.INGREDIENTS_LIST[0]['name']
        burger.add_ingredient(
            ingredient_mock
        )
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].type == TestData.INGREDIENTS_LIST[0]['type']
        assert burger.ingredients[0].name == TestData.INGREDIENTS_LIST[0]['name']
        assert burger.ingredients[0].price == TestData.INGREDIENTS_LIST[0]['price']

    def test_add_ingredient_one_more_ingredient_success(self):
        burger = Burger()
        first_ingredient_mock = Mock(**TestData.INGREDIENTS_LIST[0])
        first_ingredient_mock.name = TestData.INGREDIENTS_LIST[0]['name']
        burger.add_ingredient(
            first_ingredient_mock
        )
        second_ingredient_mock = Mock(**TestData.INGREDIENTS_LIST[1])
        second_ingredient_mock.name = TestData.INGREDIENTS_LIST[1]['name']
        burger.add_ingredient(
            second_ingredient_mock
        )
        assert len(burger.ingredients) == 2
        assert burger.ingredients[1].type == TestData.INGREDIENTS_LIST[1]['type']
        assert burger.ingredients[1].name == TestData.INGREDIENTS_LIST[1]['name']
        assert burger.ingredients[1].price == TestData.INGREDIENTS_LIST[1]['price']

    def test_remove_ingredient_success(self):
        burger = Burger()
        # database = Database()
        burger.ingredients = TestData.INGREDIENTS_LIST
        burger.remove_ingredient(0)
        assert len(burger.ingredients)