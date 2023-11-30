from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    def test_get_type_correct_type_shown(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot sauce", 30.4)

        assert ingredient.get_type() == "SAUCE"

    def test_get_name_correct_name_shown(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot sauce", 30.4)

        assert ingredient.get_name() == "Hot sauce"

    def test_get_price_correct_price_shown(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Hot sauce", 30.4)

        assert ingredient.get_price() == 30.4