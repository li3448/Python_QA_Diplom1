from praktikum.ingredient import Ingredient
import pytest


# tests ingredient.py methods
class TestIngredient:
    # test get_price for an ingredient
    @pytest.mark.parametrize('ingredient_type, ingredient_name , ingredient_price',
                             [["соус", "острый", 1389], ["начинка", "много мяса", 445.66]])
    def test_get_price_returns_ingredient_price(self, ingredient_type, ingredient_name, ingredient_price):
        test_bun = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        bun_price = test_bun.get_price()
        assert bun_price == ingredient_price

    # test get_name for an ingredient
    @pytest.mark.parametrize('ingredient_type, ingredient_name , ingredient_price',
                             [["соус", "shiny2000", 2000.11], ["начинка", "R2-D2", 111222]])
    def test_get_name_returns_ingredient_name(self, ingredient_type, ingredient_name, ingredient_price):
        test_bun = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        bun_name = test_bun.get_name()
        assert bun_name == ingredient_name

    # test get_type for an ingredient
    @pytest.mark.parametrize('ingredient_type, ingredient_name , ingredient_price',
                             [["соус", "rhd4672", 113-77], ["начинка", "lhalkhjfal-11", 300+600]])
    def test_get_type_returns_ingredient_type(self, ingredient_type, ingredient_name, ingredient_price):
        test_bun = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        bun_type = test_bun.get_type()
        assert bun_type == ingredient_type
