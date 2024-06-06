class TestDatabase:
    def test_available_buns(self, mock_database_available_buns):
        assert len(mock_database_available_buns.available_buns()) == 5

    def test_available_ingredients(self, mock_database_available_ingredients):
        assert len(mock_database_available_ingredients.available_buns()) == 4
