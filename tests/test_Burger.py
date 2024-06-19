from unittest.mock import Mock
from conftest import cosmic_burger
from burger import Burger


class TestBurger:
    def test_set_buns(self, cosmic_burger):
        mock_bun = Mock()
        # Burger().set_buns(mock_bun)
        cosmic_burger.set_buns(mock_bun)
        assert cosmic_burger.bun == mock_bun



        # set_bulka = Burger()
        # bulka = set_bulka.set_buns('hamburger')
        # assert bulka == 'hamburger'

    def test_add_ingridient(self, cosmic_burger):
        mock_ingridient = Mock()
        cosmic_burger.add_ingredient(mock_ingridient)
        assert cosmic_burger.ingredients[0] == mock_ingridient


    def test_remove_ingridient(self, cosmic_burger):
        mock_ingridient = Mock()
        cosmic_burger.add_ingredient(mock_ingridient)
        cosmic_burger.remove_ingredient(0)
        assert cosmic_burger.ingredients == []

    def test_move_ingredient(self,cosmic_burger):
        mock_ingridient_1 = Mock()
        cosmic_burger.add_ingredient(mock_ingridient_1)
        mock_ingridient_2 = Mock()
        cosmic_burger.add_ingredient(mock_ingridient_2)
        cosmic_burger.move_ingredient(0,1)
        assert cosmic_burger.ingredients[1] == mock_ingridient_1



    def test_get_price(self,cosmic_burger):
        mock_bun = Mock()#Экземпляр булки
        mock_bun.get_price.return_value = 500#Установил цену для булки
        mock_ingredient = Mock() #Сделал экземпляр ингридиента
        mock_ingredient.get_price.return_value = 1000 #Установил цену для ингредиента
        cosmic_burger.bun = mock_bun #Установил значение атрибута bun = 500
        cosmic_burger.ingredients = [mock_ingredient]#
        assert cosmic_burger.get_price() == 500 * 2 + 1000


    #
    def test_get_receipt(self, cosmic_burger):
        mock_bun = Mock()  # Экземпляр булки
        mock_bun.get_price.return_value = 500  # Установил цену для булки
        mock_ingredient = Mock()  # Сделал экземпляр ингридиента
        mock_ingredient.get_price.return_value = 1000  # Установил цену для ингредиента
        cosmic_burger.bun = mock_bun  # Установил значение атрибута bun = 500
        cosmic_burger.ingredients = [mock_ingredient]  #
        receipt = cosmic_burger.get_receipt()

        assert f'Price: 2000' in receipt