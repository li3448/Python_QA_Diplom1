from praktikum.database import Database

# tests database.py methods
class TestDatabase:
    # tests available_buns() returns the list of buns added in DB
    def test_available_buns_returns_correct_list(self):
        test_database = Database()
        assert len(test_database.available_buns()) == 3
        assert test_database.available_buns()[0].get_name() == "black bun"
        assert test_database.available_buns()[1].get_price() == 200

    # tests available_ingredients() returns the list of ingredients added in DB
    def test_available_ingredients_returns_correct_list(self):
        test_database = Database()
        assert len(test_database.available_ingredients()) == 6
        assert test_database.available_ingredients()[2].get_name() == "chili sauce"
        assert test_database.available_ingredients()[3].get_price()== 100
        assert test_database.available_ingredients()[4].type == "FILLING"
