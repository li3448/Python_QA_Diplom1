import unittest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import *

class TestBurger(unittest.TestCase):
    def setUp(self):
        self.burger = Burger()

    def test_set_buns(self):
        # Проверяем, что у булочки с ожидаемые название и цена
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булка"
        mock_bun.get_price.return_value = 100

        self.burger.set_buns(mock_bun)

        self.assertEqual(self.burger.bun.get_name(), "Булка")
        self.assertEqual(self.burger.bun.get_price(), 100)

    def test_add_ingredient(self):
        # Проверяем, что добавляется ингредиент с ожидаемым названием, типом и ценой
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "котлетка"
        mock_ingredient.get_type.return_value = "Мясо"
        mock_ingredient.get_price.return_value = 50

        self.burger.add_ingredient(mock_ingredient)

        self.assertEqual(len(self.burger.ingredients), 1)
        self.assertEqual(self.burger.ingredients[0].get_name(), "котлетка")
        self.assertEqual(self.burger.ingredients[0].get_type(), "Мясо")
        self.assertEqual(self.burger.ingredients[0].get_price(), 50)

    def test_remove_ingredient(self):
        # Проверяем, что ингридиент удаляется
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()

        burger = Burger()
        self.burger.add_ingredient(mock_ingredient1)
        self.burger.add_ingredient(mock_ingredient2)
        self.burger.remove_ingredient(0)

        assert mock_ingredient1 not in burger.ingredients

    def test_move_ingredient(self):
        #проверяем что ингридиент перемещается
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()

        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient2, mock_ingredient1]


    def test_get_receipt(self):
        #проверяем, что возвращается ожидаемый чек
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булка"
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_1.get_name.return_value = 'соус'
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_2.get_name.return_value = 'начинка'
        mock_burger = Mock()
        mock_burger.get_price.return_value = 500
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]
        burger.get_price = mock_burger.get_price
        expected_result = '(==== Булка ====)\n' \
                          '= sauce соус =\n' \
                          '= filling начинка =\n' \
                          '(==== Булка ====)\n' \
                          '\nPrice: 500'
        assert burger.get_receipt() == expected_result


