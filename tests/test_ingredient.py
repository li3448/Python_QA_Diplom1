from data import TestData


class TestIngredient:

    def test_ingredient_get_name(self):
        assert TestData.ingredient.get_name() == 'Соус Экстратеррестрис', 'Unable to get ingredient name'

    def test_ingredient_get_price(self):
        assert TestData.ingredient.get_price() == 3000, 'Unable to get ingredient price'

    def test_ingredient_get_type(self):
        assert TestData.ingredient.get_type() == 'SAUCE', 'Unable to get ingredient type'
