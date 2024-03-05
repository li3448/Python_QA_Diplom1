from praktikum.database import Database

""" Тесты для класса Database """
class TestDatabase:
    """Тест на доступные булки"""
    def test_available_buns(self):
        # Создаем объект базы данных
        database = Database()
        # Проверяем, что количество доступных булок равно 3
        assert len(database.available_buns()) == 3
        # Проверяем, что третья доступная булка имеет название "red bun"
        assert database.available_buns()[2].get_name() == "red bun"
        # Проверяем, что цена третьей доступной булки равна 300
        assert database.available_buns()[2].get_price() == 300

    """ Тест на доступные ингредиенты """
    def test_available_ingredients(self):
        # Создаем объект базы данных
        database = Database()
        # Проверяем, что количество доступных ингредиентов равно 6
        assert len(database.available_ingredients()) == 6
        # Проверяем, что третий доступный ингредиент имеет название "chili sauce"
        assert database.available_ingredients()[2].get_name() == "chili sauce"
        # Проверяем, что цена третьего доступного ингредиента равна 200
        assert database.available_ingredients()[2].get_price() == 300
