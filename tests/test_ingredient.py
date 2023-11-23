from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price_ingredient(self):
        ingredient = Ingredient('SAUCE', 'Соус', 125)
        assert ingredient.get_price() == 125, 'Неправильная цена соуса'

    def test_get_name_ingredient(self):
        ingredient = Ingredient('FILLING', 'Начинка', 155)
        assert ingredient.get_name() == 'Начинка', 'Направильное название начинки'

    def test_get_type_ingredient(self):
        ingredient = Ingredient('SAUCE', 'Соус', 125)
        assert ingredient.get_type() == 'SAUCE', 'Неверный тип ингредиента'
