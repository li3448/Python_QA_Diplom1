import pytest

from helpers import Helpers
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


class TestBurger:

    def test_burger_object_has_none_bun_attribute(self):

        burger = Burger()

        assert burger.bun is None

    def test_burger_object_has_empty_ingredients_list(self):

        burger = Burger()

        assert burger.ingredients == []

    def test_set_buns_return_bun_object(self):

        buns = Bun(Helpers.BULICHKA['name'], Helpers.BULICHKA['price'])
        burger = Burger()

        burger.set_buns(buns)

        assert burger.bun == buns

    @pytest.mark.parametrize('ingredient_type, ingredient_name, price', [
        [Helpers.SOUSETS['ingredient_type'], Helpers.SOUSETS['name'], Helpers.SOUSETS['price']],
        [Helpers.LUCHOK['ingredient_type'], Helpers.LUCHOK['name'], Helpers.LUCHOK['price']]
    ])
    def test_add_ingredient_return_list_with_assigned_ingredient(self, ingredient_type, ingredient_name, price):

        ingredient = Ingredient(ingredient_type, ingredient_name, price)
        burger = Burger()

        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_return_empty_ingredients_list(self):

        sousets = Ingredient(Helpers.SOUSETS['ingredient_type'], Helpers.SOUSETS['name'], Helpers.SOUSETS['price'])
        burger = Burger()

        burger.add_ingredient(sousets)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_return_mixed_list(self):

        #  Создаем объекты класса Ингредиент – соусец и лучок, а также объект класса Бургер
        ingredient1 = Ingredient(Helpers.SOUSETS['ingredient_type'], Helpers.SOUSETS['name'], Helpers.SOUSETS['price'])
        ingredient2 = Ingredient(Helpers.LUCHOK['ingredient_type'], Helpers.LUCHOK['name'], Helpers.LUCHOK['price'])
        burger = Burger()

        #  Добавляем в бургер ингредиенты: сначала соусец, затем лучок
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        #  Перемещаем соусец с первого на второе место в списке ингредиентов
        burger.move_ingredient(0, 1)

        #  Проверяем, что соусец теперь действительно изменил свой индекс
        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price_return_amount_of_bun_double_price_and_ingredients_price(self):

        ingredient1 = Ingredient(Helpers.SOUSETS['ingredient_type'], Helpers.SOUSETS['name'], Helpers.SOUSETS['price'])
        ingredient2 = Ingredient(Helpers.LUCHOK['ingredient_type'], Helpers.LUCHOK['name'], Helpers.LUCHOK['price'])
        bun = Bun(Helpers.BULICHKA['name'], Helpers.BULICHKA['price'])
        burger = Burger()

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        assert \
            burger.get_price() == Helpers.LUCHOK['price'] + Helpers.SOUSETS['price'] + (Helpers.BULICHKA['price'] * 2)

    def test_get_receipt_return_string_with_buns_ingredients_and_amount_price_of_burger(self):

        ingredient1 = Ingredient(Helpers.SOUSETS['ingredient_type'], Helpers.SOUSETS['name'], Helpers.SOUSETS['price'])
        ingredient2 = Ingredient(Helpers.LUCHOK['ingredient_type'], Helpers.LUCHOK['name'], Helpers.LUCHOK['price'])
        bun = Bun(Helpers.BULICHKA['name'], Helpers.BULICHKA['price'])
        burger = Burger()

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        amount_price = Helpers.LUCHOK['price'] + Helpers.SOUSETS['price'] + (Helpers.BULICHKA['price'] * 2)

        result = f'(==== {Helpers.BULICHKA["name"]} ====)\n' \
                 f'= {Helpers.SOUSETS["ingredient_type"].lower()} {Helpers.SOUSETS["name"]} =\n' \
                 f'= {Helpers.LUCHOK["ingredient_type"].lower()} {Helpers.LUCHOK["name"]} =\n' \
                 f'(==== {Helpers.BULICHKA["name"]} ====)\n' \
                 f'\nPrice: {amount_price}'

        assert burger.get_receipt() == result
