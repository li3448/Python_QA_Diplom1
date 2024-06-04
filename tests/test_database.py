# Проверки класса Database без моков
class TestDatabase:
    def test_available_buns_len_is_three(self, database_instance):
        assert len(database_instance.available_buns()) == 3

    def test_available_ingredients_len_is_six(self, database_instance):
        assert len(database_instance.available_ingredients()) == 6
