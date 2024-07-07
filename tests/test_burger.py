from conftest import *


def test_set_buns(bun):
    burger = Burger()
    burger.set_buns(bun)
    assert burger.bun == bun


def test_add_ingredient(ingredient1):
    burger = Burger()
    burger.add_ingredient(ingredient1)
    assert burger.ingredients == [ingredient1]


def test_remove_ingredient(ingredient1, ingredient2):
    burger = Burger()
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.remove_ingredient(0)
    assert burger.ingredients == [ingredient2]


def test_move_ingredient(ingredient1, ingredient2):
    burger = Burger()
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients == [ingredient2, ingredient1]


def test_get_price(bun, ingredient1, ingredient2):
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    assert burger.get_price() == 6.50


def test_get_receipt(burger):
    receipt = burger.get_receipt()
    expected_receipt = (
        "(==== Sesame Bun ====)\n"
        "= filling beef patty =\n"
        "= sauce ketchup =\n"
        "(==== Sesame Bun ====)\n\n"
        "Price: 6.5"
    )
    assert receipt == expected_receipt


@pytest.mark.parametrize("ingredient_type, name, price, expected_receipt", [
    ("filling", "lettuce", 0.30, "(==== Sesame Bun ====)\n= filling lettuce =\n(==== Sesame Bun ====)\n\nPrice: 3.3"),
    ("sauce", "mayo", 0.20, "(==== Sesame Bun ====)\n= sauce mayo =\n(==== Sesame Bun ====)\n\nPrice: 3.2")
])
def test_dynamic_receipt(bun, ingredient_type, name, price, expected_receipt):
    ingredient = Ingredient(ingredient_type, name, price)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    receipt = burger.get_receipt()
    assert receipt == expected_receipt

