from practicum.burger import Burger
from practicum.bun import Bun
import pytest
import allure
from data import *
from unittest.mock import Mock
from practicum.ingredient import Ingredient


class TestBurger:

    @allure.title('Проверка имени для установленной булки у бургера')
    def test_set_buns_name(self):
        mock_bun = Mock()
        mock_bun.configure_mock(name=BurgerData.bun_name, price=BurgerData.bun_price_1)
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == BurgerData.bun_name

    @allure.title('Проверка цены для установленной булки у бургера')
    def test_set_buns_price(self):
        mock_bun = Mock()
        mock_bun.configure_mock(name=BurgerData.bun_name, price=BurgerData.bun_price_1)
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.price == BurgerData.bun_price_1

    @allure.title('Проверка добавлениея ингредиента к бургеру')
    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(ingredient_type=BurgerData.ingredient_type_filling,
                                name=BurgerData.ingredient_name_filling,
                                price=BurgerData.ingredient_price_filling)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

    @allure.title('Проверка удаления ингредиента из бургера')
    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(ingredient_type=BurgerData.ingredient_type_filling,
                                name=BurgerData.ingredient_name_filling,
                                price=BurgerData.ingredient_price_filling)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @allure.title('Проверка изменения индекса у ингредиентов в бургере')
    def test_move_ingredient(self):
        burger = Burger()
        ingredient_0 = Ingredient(ingredient_type=BurgerData.ingredient_type_filling,
                                  name=BurgerData.ingredient_name_filling,
                                  price=BurgerData.ingredient_price_filling)
        burger.add_ingredient(ingredient_0)
        ingredient_1 = Ingredient(ingredient_type=BurgerData.ingredient_type_sauce,
                                  name=BurgerData.ingredient_name_sauce,
                                  price=BurgerData.ingredient_price_sauce)
        burger.add_ingredient(ingredient_1)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient_1
        assert burger.ingredients[1] == ingredient_0

    @allure.title('Проверка получения цены целого бургера из ингредиентов и булки')
    @pytest.mark.parametrize('bun_price, ingredient_1_price, ingredient_2_price', [[10, 20, 30], [9.9, 19.9, 29.9]])
    def test_get_price_of_burger(self, bun_price, ingredient_1_price, ingredient_2_price):
        mock_bun = Mock()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient_1.get_price.return_value = ingredient_1_price
        mock_ingredient_2.get_price.return_value = ingredient_2_price
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.extend([mock_ingredient_1, mock_ingredient_2])
        expected_result = (bun_price * 2 + ingredient_1_price + ingredient_2_price)
        actual_result = burger.get_price()
        assert expected_result == actual_result

    @allure.title('Проверка получения чека')
    def test_get_receipt(self):
        bun = Bun(BurgerData.bun_name, BurgerData.bun_price_1)
        ingredient_1 = Ingredient(ingredient_type=BurgerData.ingredient_type_filling,
                                  name=BurgerData.ingredient_name_filling,
                                  price=BurgerData.ingredient_price_filling)
        ingredient_2 = Ingredient(ingredient_type=BurgerData.ingredient_type_sauce,
                                  name=BurgerData.ingredient_name_sauce,
                                  price=BurgerData.ingredient_price_sauce)
        burger = Burger()
        burger.set_buns(bun)
        burger.ingredients.extend([ingredient_1, ingredient_2])
        expected_result = '\n'.join([f'(==== {BurgerData.bun_name} ====)',
                                     f'= {BurgerData.ingredient_type_filling.lower()} {BurgerData.ingredient_name_filling} =',
                                     f'= {BurgerData.ingredient_type_sauce.lower()} {BurgerData.ingredient_name_sauce} =',
                                     f'(==== {BurgerData.bun_name} ====)\n',
                                     f'Price: {BurgerData.burger_price_99}'])
        actual_result = burger.get_receipt()
        assert actual_result == expected_result

