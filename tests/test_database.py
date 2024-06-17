from database import Database


def test_database():
    database = Database()

    assert len(database.available_buns()) == 3 and len(database.available_ingredients()) == 6
