import sys, os

python_path = os.path.join(os.getcwd())
sys.path.append(python_path)
os.environ["PYTHONPATH"] = python_path

from praktikum.ingredient import Ingredient

class TestIngredient:
    def test_ingredient_name(self):
        ingredient = Ingredient('овощь', 'томат', 60)
        assert ingredient.get_name() == 'томат'

    def test_incorrect_ingredient_name(self):
        ingredient = Ingredient('овощь', 'томат', 60)
        assert ingredient.get_name() != 'огурец'

    def test_ingredient_price(self):
        ingredient = Ingredient('овощь', 'томат', 60)
        assert ingredient.get_price() == 60

    def test_incorrect_ingredient_price(self):
        ingredient = Ingredient('овощь', 'томат', 60)
        assert ingredient.get_price() != 90

    def test_ingredient_type(self):
        ingredient = Ingredient('овощь', 'томат', 60)
        assert ingredient.get_type() == 'овощь'

    def test_incorrect_ingredient_type(self):
        ingredient = Ingredient('овощь', 'томат', 60)
        assert ingredient.get_type() != 'фрукт'