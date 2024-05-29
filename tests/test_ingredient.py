from ingredient import Ingredient
from data import IngrData
import ingredient_types


class TestIngredient:

    def test_get_price_ingredient(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, IngrData.ingr_name, IngrData.ingr_price)
        assert ingredient.get_price() == IngrData.ingr_price and ingredient.get_type() == 'SAUCE'

    def test_get_name_ingredient(self, set_data_ingr):
        assert set_data_ingr.get_name() == IngrData.ingr_name

    def test_get_type_ingredient(self, set_data_ingr):
        assert set_data_ingr.get_type() == 'FILLING'
