from practicum.burger import Burger
from practicum.bun import Bun
import pytest
import allure
from data import *
from unittest.mock import Mock, patch
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
