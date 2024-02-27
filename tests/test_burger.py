from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from praktikum.database import Database


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('bun_name', 100.0)
        burger.set_buns(bun)

        assert burger.bun.get_name() == 'bun_name'

    def test_add_ingredients(self):
        burger = Burger()
        ingredient = Ingredient('ingredient_type', 'name', 100.00)
        burger.add_ingredient(ingredient)

        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient('ingredient_type', 'sauce', 100.00)
        burger.add_ingredient(ingredient_1)
        ingredient_2 = Ingredient('ingredient_type', 'filling', 200.00)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(1)

        assert burger.ingredients == [ingredient_1]

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Ingredient('ingredient_type', 'sauce', 100.00)
        burger.add_ingredient(ingredient_1)
        ingredient_2 = Ingredient('ingredient_type', 'filling', 200.00)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)

        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_get_price(self):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 200.00
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 300.00
        burger = Burger()

        assert burger.get_price() == 700.00

    def test_get_receipt(self):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = 'red bun'
        mock_bun.get_price.return_value = 300.00
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = 'dinosaur'
        mock_ingredient.get_type.return_value = 'FILLING'
        mock_ingredient.get_price.return_value = 200.00
        burger = Burger()

        assert burger.get_receipt() == [f'(==== red bun ====)', f'= filling dinosaur =',
                                        f'(==== red bun ====)\n', f'Price: 800.00 ']



