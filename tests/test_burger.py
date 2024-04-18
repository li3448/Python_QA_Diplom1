from data import Values
from praktikum.burger import Burger
import copy as c

class TestBurger:

    def test_remove_ingredient(self, mocked_ingredient):
        burger = Burger()
        burger.add_ingredient(mocked_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mocked_ingredient):
        burger = Burger()
        [burger.add_ingredient(c.copy(mocked_ingredient)) for _ in range(2)]
        before_move_ingredient = burger.ingredients[0]
        burger.move_ingredient(0, 1)
        after_move_ingredient = burger.ingredients[1]
        assert before_move_ingredient == after_move_ingredient

    def test_get_price(self, mocked_bun, mocked_ingredient):
        burger = Burger()
        burger.set_buns(mocked_bun)
        burger.add_ingredient(mocked_ingredient)
        burger.add_ingredient(mocked_ingredient)
        expected_price = Values.BUN_PRICE * 2 + Values.INGREDIENT_PRICE * 2
        assert burger.get_price() == expected_price

    def test_get_receipt(self, mocked_bun, mocked_ingredient):
        burger = Burger()
        burger.set_buns(mocked_bun)
        burger.add_ingredient(mocked_ingredient)
        burger.add_ingredient(mocked_ingredient)
        assert burger.get_receipt() == Values.EXPEXTED_RECEIPT
