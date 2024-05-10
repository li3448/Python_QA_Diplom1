from practicum.database import Database
import allure


class TestDatabase:

    @allure.title('Проверка списка булок в базе данных')
    def test_available_buns(self):
        bun = Database().available_buns()
        assert len(bun) == 3

    @allure.title('Проверка списка ингредиентов в базе данных')
    def test_available_ingredients(self):
        ingredients = Database().available_ingredients()
        assert len(ingredients) == 6
