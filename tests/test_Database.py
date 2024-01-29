from praktikum.database import Database


class TestDatabase:

    def test_available_buns_expected_buns_count(self):
        db = Database()
        assert len(db.available_buns()) == 3

    def test_available_ingredients_return_expected_ingredients_count(self):
        db = Database()
        assert len(db.available_ingredients()) == 6
