from ..data import DataIngredient


class TestIngredient:

    def test_set_ingredient_type_success(self, get_ingredient):
        ingredient = get_ingredient
        assert ingredient.type == DataIngredient.ING_TYPE

    def test_get_type_success(self, get_ingredient):
        ingredient = get_ingredient
        assert ingredient.get_type() == DataIngredient.ING_TYPE

    def test_set_ingredient_name_success(self, get_ingredient):
        ingredient = get_ingredient
        assert ingredient.name == DataIngredient.ING_NAME

    def test_get_name_success(self, get_ingredient):
        ingredient = get_ingredient
        assert ingredient.get_name() == DataIngredient.ING_NAME

    def test_set_ingredient_price_success(self, get_ingredient):
        ingredient = get_ingredient
        assert ingredient.price == DataIngredient.ING_PRICE1

    def test_get_price_success(self, get_ingredient):
        ingredient = get_ingredient
        assert ingredient.get_price() == DataIngredient.ING_PRICE1
