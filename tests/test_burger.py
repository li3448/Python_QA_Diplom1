import copy
from functools import reduce
from unittest.mock import Mock, patch

import pytest

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

    # @patch('ingredient.Ingredient')
    def test_add_ingredient_success(self):
        burger = Burger()
        ingredient_mock = Mock(**TestData.INGREDIENTS_LIST[1])
        print('Ingredient Name: ', ingredient_mock.name)
        print('!!!!!!!!!!!!!!!', ingredient_mock.price)
        ingredient_mock.name = TestData.INGREDIENTS_LIST[1]['name']
        burger.add_ingredient(
            ingredient_mock
        )
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].type == TestData.INGREDIENTS_LIST[1]['type']
        assert burger.ingredients[0].name == TestData.INGREDIENTS_LIST[1]['name']
        assert burger.ingredients[0].price == TestData.INGREDIENTS_LIST[1]['price']

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
        burger.ingredients = TestData.INGREDIENTS_LIST[:]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0]['name'] == TestData.INGREDIENTS_LIST[1]['name']
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, index: int, new_index: int):
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    @pytest.mark.parametrize('item', TestData.BURGERS_LIST)
    def test_get_price(self, item):
        bun_price = item.get('bun').get('price')
        ingredient_price = sum(
            map(
                lambda x : x['price'], item['ingredients']
            )
        )
        total_price = 2 * bun_price + ingredient_price
        bun = Mock()
        bun.name = item['bun'].get('name')
        bun.price = item['bun'].get('price')
        bun.get_price.return_value = item['bun']['price']
        burger = Burger()
        burger.bun = bun
        burger.ingredients = []
        for i in item['ingredients']:
            elem = Mock()
            elem.name = i['name']
            elem.price = i['price']
            elem.type = i['type']
            elem.get_price.return_value = i['price']
            burger.ingredients.append(elem)
        assert burger.get_price() == total_price
