import pytest

from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("Соусы", "Соус Spicy-X", 90),
        ("Начинки", "Говяжий метеорит (отбивная)", 3000),
    ])
    def test_for_get_price_method(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("Соусы", "Соус Spicy-X", 90),
        ("Начинки", "Говяжий метеорит (отбивная)", 3000),
    ])
    def test_for_get_name_method(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("Соусы", "Соус Spicy-X", 90),
        ("Начинки", "Говяжий метеорит (отбивная)", 3000),
    ])
    def test_for_get_type_method(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
