from ingredient_types import *
from conftest import *


def test_available_buns(database):
    buns = database.available_buns()
    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"
    assert buns[0].get_price() == 100
    assert buns[1].get_name() == "white bun"
    assert buns[1].get_price() == 200
    assert buns[2].get_name() == "red bun"
    assert buns[2].get_price() == 300


def test_available_ingredients(database):
    ingredients = database.available_ingredients()
    assert len(ingredients) == 6

    sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
    fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]

    assert len(sauces) == 3
    assert sauces[0].get_name() == "hot sauce"
    assert sauces[0].get_price() == 100
    assert sauces[1].get_name() == "sour cream"
    assert sauces[1].get_price() == 200
    assert sauces[2].get_name() == "chili sauce"
    assert sauces[2].get_price() == 300

    assert len(fillings) == 3
    assert fillings[0].get_name() == "cutlet"
    assert fillings[0].get_price() == 100
    assert fillings[1].get_name() == "dinosaur"
    assert fillings[1].get_price() == 200
    assert fillings[2].get_name() == "sausage"
    assert fillings[2].get_price() == 300


@pytest.mark.parametrize("name, price", [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
])
def test_bun_creation(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price


@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (INGREDIENT_TYPE_FILLING, "sausage", 300)
])
def test_ingredient_creation(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price

