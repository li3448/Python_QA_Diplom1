import copy
from unittest.mock import Mock, patch

import pytest

from burger import Burger
from data.data import TestData
from tests.helper_funcs import HelperFuncs


class TestBurger:

    def test_default_bun_none_true(self):
        burger = Burger()
        assert burger.bun == None

    def test_default_ingredients_empty_list_true(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        burger.set_buns(TestData.BUNS_LIST[0])
        assert burger.bun == TestData.BUNS_LIST[0]

    def test_set_another_buns_true(self):
        burger = Burger()
        burger.set_buns(TestData.BUNS_LIST[0])
        burger.set_buns(TestData.BUNS_LIST[1])
        assert burger.bun == TestData.BUNS_LIST[1]

    def test_add_ingredient_success(self):
        burger = Burger()
        ingredient_mock = Mock(**TestData.INGREDIENTS_LIST[1])
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
        burger.ingredients = TestData.INGREDIENTS_LIST[:]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0]['name'] == TestData.INGREDIENTS_LIST[1]['name']
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @pytest.mark.parametrize('item', TestData.BURGERS_LIST[3:])
    def test_move_ingredient_move_last_to_first_success(self, item):
        burger = HelperFuncs.create_burger_instance(item)
        initial_burger_ingredients_list = copy.deepcopy(burger.ingredients)
        last_ingredient = burger.ingredients[len(burger.ingredients) - 1]
        burger.move_ingredient(len(burger.ingredients) - 1, 0)
        assert burger.ingredients[0] == last_ingredient
        assert burger.ingredients[1:] == initial_burger_ingredients_list[0: -1]

    @pytest.mark.parametrize('item', TestData.BURGERS_LIST[3:])
    def test_move_ingredient_move_first_to_last_success(self, item):
        burger = HelperFuncs.create_burger_instance(item)
        initial_burger_ingredients_list = copy.deepcopy(burger.ingredients)
        first_ingredient = burger.ingredients[0]
        burger.move_ingredient(0, len(burger.ingredients) - 1)
        assert burger.ingredients[len(burger.ingredients) - 1] == first_ingredient
        assert initial_burger_ingredients_list[1:] == burger.ingredients[0: -1]

    @pytest.mark.parametrize('item', TestData.BURGERS_LIST)
    def test_get_price_success(self, item):
        total_price = HelperFuncs.get_burger_price(item)
        burger = HelperFuncs.create_burger_instance(item)
        assert burger.get_price() == total_price

    @patch('burger.Burger.get_price')
    @pytest.mark.parametrize('item', TestData.BURGERS_LIST[0:])
    def test_get_receipt(self, mock_get_price, item): #  item,
        mock_get_price.return_value = HelperFuncs.get_burger_price(item)
        burger = HelperFuncs.create_burger_instance(item)
        receipt = burger.get_receipt()
        receipt_strs_array = HelperFuncs.split_text_by_lines(receipt)

        receipt_strs_array_length = len(receipt_strs_array)
        # check if bun lines are equal
        assert receipt_strs_array[0] == receipt_strs_array[receipt_strs_array_length - 2]
        # check bun line format
        assert receipt_strs_array[0] == f'(==== {item.get('bun').get('name')} ====)'
        ingredient_str_array = HelperFuncs.get_ingredient_strings_from_receipt(receipt_strs_array)
        # check ingredient lines quantity
        assert len(ingredient_str_array) == len(item.get('ingredients'))

        for s, item_ingredient in zip(ingredient_str_array, item.get('ingredients')):
            # check ingredient line format
            assert s == f'= {item_ingredient.get('type').lower()} {item_ingredient.get('name')} ='
        # check price line format
        assert receipt_strs_array[receipt_strs_array_length - 1] == \
            f'Price: {HelperFuncs.get_burger_price(item)}'
