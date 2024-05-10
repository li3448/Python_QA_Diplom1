from practicum.database import Database


class TestDatabase:

    def test_available_buns(self):
        bun = Database().available_buns()
        assert len(bun) == 3

    def test_available_ingredients(self):
        ingredients = Database().available_ingredients()
        assert len(ingredients) == 6