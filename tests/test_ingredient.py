import pytest
from ingredient import Ingredient


@pytest.mark.parametrize(
    "ingredient_type, name, price",
    [
        ("filling", "cheese", 1.50),
        ("sauce", "tomato", 0.75),
        ("filling", "ham", 2.00),
        ("sauce", "mayonnaise", 0.50)
    ]
)
def test_ingredient_creation(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.type == ingredient_type
    assert ingredient.name == name
    assert ingredient.price == price


@pytest.mark.parametrize(
    "price",
    [
        1.50,
        0.75,
        2.00,
        0.50
    ]
)
def test_get_price(price):
    ingredient = Ingredient("filling", "test", price)
    assert ingredient.get_price() == price


@pytest.mark.parametrize(
    "name",
    [
        "cheese",
        "tomato",
        "ham",
        "mayonnaise"
    ]
)
def test_get_name(name):
    ingredient = Ingredient("filling", name, 1.00)
    assert ingredient.get_name() == name


@pytest.mark.parametrize(
    "ingredient_type",
    [
        "filling",
        "sauce"
    ]
)
def test_get_type(ingredient_type):
    ingredient = Ingredient(ingredient_type, "test", 1.00)
    assert ingredient.get_type() == ingredient_type
