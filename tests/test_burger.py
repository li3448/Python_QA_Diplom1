import pytest
from unittest.mock import Mock

import data.mock_variables as mock_var
from praktikum.burger import Burger


class TestBurger:
    def test_burger_init(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    @pytest.mark.parametrize('bun_name', ['Флюоресцентная булка', 'Краторная булка'])
    def test_set_buns(self, bun_name):
        burger = Burger()
        assert burger.bun == burger.set_buns(bun_name)

    @pytest.mark.parametrize('ingredient', ['Соус с шипами Антарианского плоскоходца', 'Говяжий метеорит (отбивная)'])
    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize('ingredient_1, ingredient_2',
                             [
                                ('Соус с шипами Антарианского плоскоходца', 'Говяжий метеорит (отбивная)'),
                                ('Соус традиционный галактический', 'Биокотлета из марсианской Магнолии'),
                             ])
    def test_remove_ingredient(self, ingredient_1, ingredient_2):
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_2]

    @pytest.mark.parametrize('ingredient_1, ingredient_2',
                             [
                                ('Соус с шипами Антарианского плоскоходца', 'Говяжий метеорит (отбивная)'),
                                ('Соус традиционный галактический', 'Биокотлета из марсианской Магнолии'),
                             ])
    def test_move_ingredient(self, ingredient_1, ingredient_2):
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == ([ingredient_2] + [ingredient_1])

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_ingredient = Mock()

        mock_bun.get_price.return_value = mock_var.mock_bun_price
        mock_ingredient.get_price.return_value = mock_var.mock_ingredient_price

        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == mock_var.mock_bun_price * 2 + mock_var.mock_ingredient_price

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_self = Mock()

        mock_bun.get_name.return_value = mock_var.mock_bun_name
        mock_ingredient.get_name.return_value = mock_var.mock_ingredient_name
        mock_ingredient.get_type.return_value = mock_var.mock_ingredient_type
        mock_self.get_price.return_value = mock_var.mock_self_price

        burger.get_price = mock_self.get_price
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]

        assert (burger.get_receipt() ==
                "(==== Краторная булка N-200i ====)\n"
                "= котлета Плоды Фалленианского дерева =\n"
                "(==== Краторная булка N-200i ====)\n\n"
                "Price: 1255")
