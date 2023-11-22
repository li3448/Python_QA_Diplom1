import sys, os

python_path = os.path.join(os.getcwd())
sys.path.append(python_path)
os.environ["PYTHONPATH"] = python_path

import pytest

class TestBurger:
    def test_set_buns_with_mock(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient_with_mock(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient_with_mock(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert ingredient_mock not in burger.ingredients

    @pytest.mark.parametrize('index, new_index', [(0, 1), (1, 0)])
    def test_move_ingredient_with_mock(self, burger, ingredient_mock, index, new_index):
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(ingredient_mock)
        original_ingredient = burger.ingredients[index]
        burger.move_ingredient(index, new_index)
        assert original_ingredient == burger.ingredients[new_index]

    def test_get_price_with_mocks(self, burger, bun_mock, ingredient_mock):
        bun_mock.get_price.return_value = 1.0
        ingredient_mock.get_price.return_value = 1.0
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == 4.0

    def test_get_receipt_with_mocks(self, burger, bun_mock, ingredient_mock):
        bun_mock.get_name.return_value = 'Tasty Bun'
        ingredient_mock.get_type.return_value = 'Sauce'
        ingredient_mock.get_name.return_value = 'Mayonnaise'
        bun_mock.get_price.return_value = 1.0
        ingredient_mock.get_price.return_value = 1.0
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(ingredient_mock)
        expected_receipt = '(==== Tasty Bun ====)\n= sauce Mayonnaise =\n= sauce Mayonnaise =\n(==== Tasty Bun ====)\n\nPrice: 4.0'
        assert burger.get_receipt() == expected_receipt