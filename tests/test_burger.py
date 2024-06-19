from helpers.generate import generate_burger, generate_ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_burger_get_price_with_one_ingredient(self):
        burger = generate_burger()

        ingredient = generate_ingredient()

        burger.add_ingredient(ingredient)

        assert burger.get_price() == burger.bun.get_price() * 2 + ingredient.get_price()

    def test_burger_get_price_with_without_ingredient(self):
        burger = generate_burger()

        assert burger.get_price() == burger.bun.get_price() * 2

    def test_burger_get_price_with_remove_ingredient(self):
        burger = generate_burger()

        ingredient = generate_ingredient()

        burger.add_ingredient(ingredient)

        price_burger_with_ingredient = burger.get_price()

        burger.remove_ingredient(0)

        price_burger_without_ingredient = burger.get_price()

        assert price_burger_without_ingredient != price_burger_with_ingredient

    def test_burger_get_receipt(self):
        burger = generate_burger()

        ingredient = generate_ingredient()

        burger.add_ingredient(ingredient)

        receipt = [f'(==== {burger.bun.get_name()} ====)',
                   f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =',
                   f'(==== {burger.bun.get_name()} ====)\n', f'Price: {burger.get_price()}']

        assert burger.get_receipt() == '\n'.join(receipt)

    def test_burger_get_receipt_move_ingredient(self):
        burger = generate_burger()

        ingredient_sauce = generate_ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE)

        burger.add_ingredient(ingredient_sauce)

        ingredient_filling = generate_ingredient(ingredient_type=INGREDIENT_TYPE_FILLING)

        burger.add_ingredient(ingredient_filling)

        receipt = burger.get_receipt()

        burger.move_ingredient(0, 1)

        receipt_move_ingredient = burger.get_receipt()

        assert receipt != receipt_move_ingredient
