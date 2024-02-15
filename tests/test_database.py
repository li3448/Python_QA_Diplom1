from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()

        assert len(database.available_buns()) == 3
        assert database.available_buns()[0].get_name() == "black bun"

    def test_available_ingredients(self):
        database = Database()

        assert len(database.available_ingredients()) == 6
        assert database.available_ingredients()[0].get_name() == "hot sauce"
