
class TestIngredient:
    def test_get_price(self, ingredient):
        # Проверяем, что метод get_price возвращает ожидаемую цену
        assert ingredient.get_price() == 0.75

    def test_get_name(self, ingredient):
        # Проверяем, что метод get_name возвращает ожидаемое название
        assert ingredient.get_name() == "Tomato"

    def test_get_type(self, ingredient, sauce):
        # Проверяем, что метод get_type возвращает ожидаемый тип для двух разных фикстур
        assert ingredient.get_type() == "filling"
        assert sauce.get_type() == "sauce"