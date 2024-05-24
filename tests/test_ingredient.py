from ingredient import Ingredient


class TestIngredientFunction:
    def test_ingredient_get_price(self):
        fill = Ingredient('Начинка', 'Мясо бессмертных моллюсков Protostomia', 1337)
        assert fill.get_price() == 1337

    def test_ingredient_get_name(self):
        fill = Ingredient('Соус', 'Соус Spicy-X', 90)
        assert fill.get_name() == 'Соус Spicy-X'

    def test_ingredient_get_type(self):
        fill = Ingredient('Начинка', 'Кристаллы марсианских альфа-сахаридов', 762)
        assert fill.get_type() == 'Начинка'
