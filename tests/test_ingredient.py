import pytest

from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 ('Котлета', 'Плоды Фалленианского дерева', 1245),
                                 ('Сыр', 'Сыр с астероидной плесенью', 4142),
                             ])
    def test_get_price(self, ingredient_type, name, price):
        bun = Ingredient(ingredient_type, name, price)
        assert bun.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 ('Котлета', 'Плоды Фалленианского дерева', 1245),
                                 ('Сыр', 'Сыр с астероидной плесенью', 4142),
                             ])
    def test_get_name(self, ingredient_type, name, price):
        bun = Ingredient(ingredient_type, name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price',
                             [
                                 ('Котлета', 'Плоды Фалленианского дерева', 1245),
                                 ('Сыр', 'Сыр с астероидной плесенью', 4142),
                             ])
    def test_get_type(self, ingredient_type, name, price):
        bun = Ingredient(ingredient_type, name, price)
        assert bun.get_type() == ingredient_type
