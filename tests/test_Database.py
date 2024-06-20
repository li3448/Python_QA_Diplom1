import allure

from praktikum import Database


class TestDataBase:

    @allure.description('Кол-во булок равно 3')
    def test_available_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3

    @allure.description('Кол-во ингредиентов равно 6')
    def test_available_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
