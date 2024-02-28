import pytest
from unittest.mock import Mock

from ..data import DataIngredient as DI


class TestBurger:

    def test_set_buns(self, get_burger, get_bun_mock_data):
        current_bun_name = get_bun_mock_data.name
        get_burger.set_buns(get_bun_mock_data)
        assert get_burger.bun.name == current_bun_name

    def test_add_ingredient(self, get_burger, get_ing_mock_data):
        get_burger.add_ingredient(get_ing_mock_data[0])
        assert len(get_burger.ingredients) == 1
        assert get_burger.ingredients[0].name == get_ing_mock_data[0].name

    def test_remove_ingredient(self, get_burger, get_ing_mock_data):
        get_burger.ingredients = get_ing_mock_data
        len_before = len(get_burger.ingredients)
        current_ing_name = get_burger.ingredients[0].name
        get_burger.remove_ingredient(0)
        len_after = len(get_burger.ingredients)
        assert len_before - len_after == 1
        assert current_ing_name not in get_burger.ingredients

    def test_move_ingredient(self, get_burger, get_ing_mock_data):
        get_burger.ingredients = get_ing_mock_data
        test_ing = DI.ING_NAME
        test_index = 0
        get_burger.ingredients.insert(test_index, test_ing)
        get_burger.move_ingredient(test_index, 1)
        index_after = get_burger.ingredients.index(test_ing)
        assert test_index != index_after
        assert get_burger.ingredients[test_index] != test_ing

    def test_get_price(self, get_burger, get_bun_mock_data, get_ing_mock_data, get_price_burger_mock):
        get_burger.ingredients = get_ing_mock_data
        get_burger.bun = get_bun_mock_data
        assert get_burger.get_price() == get_price_burger_mock

    @pytest.mark.parametrize('bun_price', [89.75, 202])
    @pytest.mark.parametrize('ing_price1, ing_price2', [(54.40, 75), (129.5, 87.80)])
    def test_get_price(self, get_burger, bun_price, ing_price1, ing_price2):
        mock_bun = Mock()
        mock_bun.price = mock_bun.get_price.return_value = bun_price
        get_burger.bun = mock_bun
        mock_ing1 = Mock()
        mock_ing1.price = mock_ing1.get_price.return_value = ing_price1
        mock_ing2 = Mock()
        mock_ing2.price = mock_ing2.get_price.return_value = ing_price2
        get_burger.ingredients = [mock_ing1, mock_ing2]
        burger_price = bun_price*2 + ing_price1 + ing_price2
        assert get_burger.get_price() == burger_price

    def test_get_receipt(self, get_burger, get_bun_mock_data, get_ing_mock_data, get_price_burger_mock):
        get_burger.ingredients = get_ing_mock_data
        get_burger.bun = get_bun_mock_data
        current_receipt = [f'(==== {get_burger.bun.name} ====)']
        for ingredient in get_burger.ingredients:
            current_receipt.append(f'= {ingredient.type.lower()} {ingredient.name} =')
        current_receipt.append(f'(==== {get_burger.bun.name} ====)\n')
        current_receipt.append(f'Price: {get_burger.get_price()}')
        current_receipt = '\n'.join(current_receipt)
        assert get_burger.get_receipt() == current_receipt
