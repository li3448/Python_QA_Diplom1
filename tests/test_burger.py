from helpers.generate import generate_burger, generate_name, generate_price
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_burger_get_price_with_one_ingredient():
    burger = generate_burger()

    ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name=generate_name(), price=generate_price())

    burger.add_ingredient(ingredient)

    assert burger.get_price() == burger.bun.get_price() * 2 + ingredient.get_price()


def test_burger_get_price_with_without_ingredient():
    burger = generate_burger()

    assert burger.get_price() == burger.bun.get_price() * 2


def test_burger_get_price_with_remove_ingredient():
    burger = generate_burger()

    ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name=generate_name(), price=generate_price())

    burger.add_ingredient(ingredient)

    price_burger_with_ingredient = burger.get_price()

    burger.remove_ingredient(0)

    price_burger_without_ingredient = burger.get_price()

    assert price_burger_without_ingredient != price_burger_with_ingredient


def test_burger_get_receipt():
    burger = generate_burger()

    ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name=generate_name(), price=generate_price())

    burger.add_ingredient(ingredient)

    receipt = [f'(==== {burger.bun.get_name()} ====)',
               f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =',
               f'(==== {burger.bun.get_name()} ====)\n', f'Price: {burger.get_price()}']

    assert burger.get_receipt() == '\n'.join(receipt)


def test_burger_get_receipt_move_ingredient():
    burger = generate_burger()

    ingredient_sauce = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name=generate_name(), price=generate_price())

    burger.add_ingredient(ingredient_sauce)

    ingredient_filling = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name=generate_name(),
                                    price=generate_price())

    burger.add_ingredient(ingredient_filling)

    receipt = burger.get_receipt()

    burger.move_ingredient(0, 1)

    receipt_move_ingredient = burger.get_receipt()

    assert receipt != receipt_move_ingredient
