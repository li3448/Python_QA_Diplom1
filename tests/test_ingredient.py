from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


def test_get_price():
    bulka = Ingredient(INGREDIENT_TYPE_SAUCE, 'Rufl', 100)
    bulka.get_price()
    assert 100 == bulka.price


#
def test_get_name():
    bulka = Ingredient(INGREDIENT_TYPE_SAUCE, 'Rufl', 100)
    bulka.get_name()
    assert 'Rufl' == bulka.name


def test_get_type():
    bulka = Ingredient(INGREDIENT_TYPE_SAUCE, 'Rufl', 100)
    bulka.get_type()
    assert 'SAUCE' == bulka.type
