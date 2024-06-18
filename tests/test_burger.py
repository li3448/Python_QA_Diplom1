import allure
import pytest

from burger import Burger
from unittest.mock import Mock, patch
from conftest import mock_white_bun, mock_red_bun, mock_sauce, mock_filling
from data import BurgerGetPrice as bp, BurgerConsist as bc


class TestBurger:
    # тесты для метода set_buns
    @allure.title('проверка добавления 1 булки')
    def test_set_buns(self, mock_white_bun):
        burger = Burger()
        burger.set_buns(mock_white_bun)

        assert (burger.bun.name == bc.FIRST_BUN_NAME and burger.bun.price == bc.FIRST_BUN_PRICE
                and burger.bun.name is not None)

    @allure.title('проверка добавление 2 булок')
    def test_set_two_buns(self, mock_white_bun, mock_red_bun):
        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.set_buns(mock_red_bun)

        assert (burger.bun.name == bc.SECOND_BUN_NAME and burger.bun.price == bc.SECOND_BUN_PRICE
                and burger.bun.name is not None)

    # тесты для метода add_ingredient
    @allure.title('проверка добавления 1 ингредиента')
    def test_add_one_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)

        assert len(burger.ingredients) == 1


    @allure.title('проверка добавления 2 ингредиентов - соус и начинка')
    def test_add_two_ingredients(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert len(burger.ingredients) == 2


    @allure.title('проверка добавления 2 соусов')
    def test_add_two_sauces(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_sauce)

        assert len(burger.ingredients) == 2


    @allure.title('проверка добавления 2 начинок')
    def test_add_two_fillings(self, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling)

        assert len(burger.ingredients) == 2

    # тесты для метода remove_ingredient
    @allure.title('проверка удаления 1 ингредиента, если добавлен 1 ингредиент')
    def test_delete_one_ingredient_in_list_with_one_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0


    @allure.title('проверка удаления 1 ингредиента, если добавлено 2 ингредиента')
    def test_delete_one_ingredient_in_list_with_two_ingredients(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)  # удаляем ингредиент с индексом 1 или 0

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].type == bc.INGREDIENT_TYPE_FILLING  # так как удалили ингредиент с индексом 0, проверяем
                                                                       # что ингредиент с индексом 1 остался в списке

    @allure.title('проверка удаления ингредиента с несуществующим индексом')
    def test_delete_ingredient_with_incorrect_index(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        try:
            burger.remove_ingredient(2)
        except IndexError:
            result = f'индекс не существует'
        return result
        assert len(burger.ingredients) == 2

    # тесты для метода move_ingredient
    @allure.title('проверка на замену местами двух ингредиентов в списке')
    @pytest.mark.parametrize('new_index, old_index', [[0, 1], [1, 0]])
    def test_move_ingredients_in_list(self, mock_sauce, mock_filling, new_index, old_index):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(new_index, old_index)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == bc.INGREDIENT_TYPE_FILLING
        assert burger.ingredients[1].type == bc.INGREDIENT_TYPE_SAUCE

    # тесты для метода get_price
    @allure.title('получение стоимости бургера с 2 булками и 2 ингредиентами')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    def test_get_price_with_two_buns_and_sauce_filling(self, mock_ingredient_class, mock_bun_class):
        mock_white_bun = Mock()
        mock_sauce = Mock()
        mock_filling = Mock()
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        mock_sauce.get_price.return_value = bc.SAUCE_PRICE
        mock_filling.get_price.return_value = bc.FILLING_PRICE
        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.get_price() == bp.TWO_BUNS_SAUCE_FILLING_PRICE # 900 = 900 цена

    @allure.title('получение стоимости бургера с 2 булками')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    def test_get_price_with_two_buns_and_sauce_filling(self, mock_ingredient_class, mock_bun_class):
        mock_white_bun = Mock()
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        burger = Burger()
        burger.set_buns(mock_white_bun)

        assert burger.get_price() == bp.TWO_BUNS_PRICE

    @allure.title('получение стоимости бургера с 2 булками и с соусом')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    def test_get_price_with_two_buns_and_sauce_filling(self, mock_ingredient_class, mock_bun_class):
        mock_white_bun = Mock()
        mock_sauce = Mock()
        mock_sauce.get_price.return_value = bc.SAUCE_PRICE
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.add_ingredient(mock_sauce)

        assert burger.get_price() == bp.BUNS_SAUCE_PRICE

    @allure.title('получение стоимости бургера с 2 булками и ингредиентом')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    def test_get_price_with_two_buns_and_sauce_filling(self, mock_ingredient_class, mock_bun_class):
        mock_white_bun = Mock()
        mock_filling = Mock()
        mock_filling.get_price.return_value = bc.SAUCE_PRICE
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.add_ingredient(mock_filling)

        assert burger.get_price() == bp.BUNS_SAUCE_PRICE

    # тесты для метода get_receipt
    @allure.title('получение рецепта полного бургера')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    @patch('burger.Burger.get_price', return_value=bp.TWO_BUNS_SAUCE_FILLING_PRICE)
    def test_get_receipt_full_burger(self, mock_burger_get_price, mock_ingredient_class, mock_bun_class):
        mock_white_bun = Mock()
        mock_sauce = Mock()
        mock_filling = Mock()
        mock_white_bun.get_name.return_value = bc.FIRST_BUN_NAME
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        mock_sauce.get_type.return_value = bc.INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = bc.INGREDIENT_TYPE_SAUCE_NAME
        mock_sauce.get_price.return_value = bc.SAUCE_PRICE
        mock_filling.get_type.return_value = bc.INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = bc.INGREDIENT_TYPE_FILLING_NAME
        mock_filling.get_price.return_value = bc.FILLING_PRICE

        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()

        assert str(bc.FIRST_BUN_NAME and bc.INGREDIENT_TYPE_SAUCE_NAME and bc.INGREDIENT_TYPE_FILLING_NAME) in receipt
        assert str(bp.TWO_BUNS_SAUCE_FILLING_PRICE) in receipt

    @allure.title('получение рецепта бургера только с булками')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    @patch('burger.Burger.get_price', return_value=bp.TWO_BUNS_PRICE)
    def test_get_receipt_full_burger(self, mock_burger_get_price, mock_ingredient_class, mock_bun_class):
        mock_white_bun = Mock()
        mock_white_bun.get_name.return_value = bc.FIRST_BUN_NAME
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        burger = Burger()
        burger.set_buns(mock_white_bun)

        receipt = burger.get_receipt()

        assert str(bc.FIRST_BUN_NAME) in receipt
        assert str(bp.TWO_BUNS_PRICE) in receipt

    @allure.title('получение рецепта бургера с булками и ингредиентом')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    @patch('burger.Burger.get_price', return_value=bp.BUNS_FILLING_PRICE)
    def test_get_receipt_full_burger(self, mock_burger_get_price, mock_ingredient_class, mock_bun_class):
        mock_white_bun = Mock()
        mock_filling = Mock()
        mock_white_bun.get_name.return_value = bc.FIRST_BUN_NAME
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        mock_filling.get_type.return_value = bc.INGREDIENT_TYPE_FILLING
        mock_filling.get_name.return_value = bc.INGREDIENT_TYPE_FILLING_NAME
        mock_filling.get_price.return_value = bc.FILLING_PRICE

        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()

        assert str(bc.FIRST_BUN_NAME and bc.INGREDIENT_TYPE_FILLING_NAME) in receipt
        assert str(bp.BUNS_FILLING_PRICE) in receipt

    @allure.title('получение рецепта бургера с булками и соусом')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    @patch('burger.Burger.get_price', return_value=bp.BUNS_SAUCE_PRICE)
    def test_get_receipt_full_burger(self, mock_burger_get_price, mock_ingredient_class, mock_bun_class):
        mock_white_bun = Mock()
        mock_sauce = Mock()
        mock_white_bun.get_name.return_value = bc.FIRST_BUN_NAME
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        mock_sauce.get_type.return_value = bc.INGREDIENT_TYPE_SAUCE
        mock_sauce.get_name.return_value = bc.INGREDIENT_TYPE_SAUCE_NAME
        mock_sauce.get_price.return_value = bc.SAUCE_PRICE

        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.add_ingredient(mock_sauce)

        receipt = burger.get_receipt()

        assert str(bc.FIRST_BUN_NAME and bc.INGREDIENT_TYPE_SAUCE_NAME) in receipt
        assert str(bp.BUNS_SAUCE_PRICE) in receipt





































