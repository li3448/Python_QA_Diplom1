from unittest.mock import Mock
from conftest import cosmic_burger


class TestBurger:
    def test_set_buns(self, cosmic_burger, mock_bun):
        cosmic_burger.set_buns(mock_bun)
        assert cosmic_burger.bun == mock_bun

    def test_add_ingredient(self, cosmic_burger, mock_ingridient):
        cosmic_burger.add_ingredient(mock_ingridient)
        assert cosmic_burger.ingredients[0] == mock_ingridient

    def test_remove_ingredient(self, cosmic_burger, mock_ingridient):
        cosmic_burger.add_ingredient(mock_ingridient)
        cosmic_burger.remove_ingredient(0)
        assert cosmic_burger.ingredients == []

    def test_move_ingredient(self, cosmic_burger):
        mock_ingredient_1 = Mock()
        cosmic_burger.add_ingredient(mock_ingredient_1)
        mock_ingredient_2 = Mock()
        cosmic_burger.add_ingredient(mock_ingredient_2)
        cosmic_burger.move_ingredient(0, 1)
        assert cosmic_burger.ingredients[1] == mock_ingredient_1

    def test_get_price(self, cosmic_burger, mock_bun):
        mock_bun.get_price.return_value = 500  # Установил цену для булки
        mock_ingredient = Mock()  # Сделал экземпляр ингридиента
        mock_ingredient.get_price.return_value = 1000  # Установил цену для ингредиента
        cosmic_burger.bun = mock_bun  # Установил значение атрибута бургера bun = 500
        cosmic_burger.ingredients = [mock_ingredient]  #
        assert cosmic_burger.get_price() == 500 * 2 + 1000


    def test_get_receipt(self, cosmic_burger, mock_bun_price):
        mock_bun_price.get_price.return_value = 500  # Установил цену для булки
        mock_ingredient_price = Mock()  # Сделал экземпляр ингридиента
        mock_ingredient_price.get_price.return_value = 1000  # Установил цену для ингредиента
        cosmic_burger.bun = mock_bun_price  # Установил значение атрибута bun = 500
        cosmic_burger.ingredients = [mock_ingredient_price]  #
        receipt = cosmic_burger.get_receipt()
        print(receipt)
        assert f'Price: 2000' in receipt
