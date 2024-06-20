from praktikum.database import Database


class TestDatabase:
    def test_buns_and_ingredients_true(self):
        database = Database()

        assert database.buns != [] and database.ingredients != []

    def test_available_buns_true(self):
        database = Database()

        assert len(database.buns) == 3

    def test_available_ingredients(self):
        database = Database()

        assert len(database.ingredients) == 6
