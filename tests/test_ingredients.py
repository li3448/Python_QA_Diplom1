from ingredient import Ingredient


class TestIngredients:
    def test_constructor_ing_type(self):
        my_ing = Ingredient('filling', 'apple', 50)
        assert my_ing.type == 'filling'

    def test_constructor_ing_name(self):
        my_ing = Ingredient('filling', 'apple', 50)
        assert my_ing.name == 'apple'

    def test_constructor_ing_price(self):
        my_ing = Ingredient('filling', 'apple', 50)
        assert my_ing.price == 50

    def test_get_ing_name(self):
        my_ing = Ingredient('filling', 'apple', 50)
        assert my_ing.get_name() == 'apple'

    def test_get_ing_price(self):
        my_ing = Ingredient('filling', 'banana', 200)
        assert my_ing.get_price() == 200

    def test_get_ing_type(self):
        my_ing = Ingredient('souse', 'milky', 200)
        assert my_ing.get_type() == 'souse'
