import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            ['SAUCE', 'Соус традиционный галактический', 15.5],
            ['FILLING', 'Мясо бессмертных моллюсков Protostomia', 250.6]
        ]
    )
    def test_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_price() == price
