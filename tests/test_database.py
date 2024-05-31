def test_available_buns(database):
    buns = database.available_buns()
    assert len(buns) == 3
    assert buns[0].name == "black bun"
    assert buns[1].name == "white bun"
    assert buns[2].name == "red bun"

def test_available_ingredients(database):
    ingredients = database.available_ingredients()
    assert len(ingredients) == 6
    assert ingredients[0].name == "hot sauce"
    assert ingredients[1].name == "sour cream"
    assert ingredients[2].name == "chili sauce"
    assert ingredients[3].name == "cutlet"
    assert ingredients[4].name == "dinosaur"
    assert ingredients[5].name == "sausage"