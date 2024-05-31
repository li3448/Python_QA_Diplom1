import pytest

def test_set_buns(burger, mock_bun):
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

def test_add_ingredient(burger, mock_ingredient):
    burger.add_ingredient(mock_ingredient)
    assert mock_ingredient in burger.ingredients

@pytest.mark.parametrize("index", [0, 1, 2])
def test_remove_ingredient(burger_with_ingredients, index):
    ingredients = burger_with_ingredients.ingredients.copy()
    burger_with_ingredients.remove_ingredient(index)
    assert len(burger_with_ingredients.ingredients) == 2
    assert ingredients[index] not in burger_with_ingredients.ingredients

def test_move_ingredient(burger_with_ingredients):
    burger_with_ingredients.move_ingredient(0, 2)
    assert burger_with_ingredients.ingredients[2].get_name() == "Ingredient 0"

def test_get_receipt(burger, mock_bun, mock_ingredient):
    expected_receipt = f"""(==== {mock_bun.get_name()} ====)
= {mock_ingredient.get_type().lower()} {mock_ingredient.get_name()} =
(==== {mock_bun.get_name()} ====)

Price: {burger.get_price()}"""
    receipt = burger.get_receipt()
    assert receipt == expected_receipt