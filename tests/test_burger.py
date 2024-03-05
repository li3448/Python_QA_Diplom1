import pytest
import praktikum.ingredient_types


from unittest.mock import Mock
from praktikum.burger import Burger, Ingredient, Bun
from praktikum.database import Database


""" Тесты для класса Burger """
class TestBurger:

    """ Тест на установку булочек """
    def test_set_buns(self):
        # Создаем экземпляр класса Burger
        burger = Burger()
        bun = Bun(name='Brioche', price=125.0)
        burger.set_buns(bun)
        assert burger.bun.get_name() == 'Brioche'

    def test_set_buns_change_bun(self):
        # Создаем экземпляр класса Burger
        burger = Burger()
        # Создаем экземпляры класса Bun с заданными параметрами
        bun1 = Bun('Black bun', 100.0)
        bun2 = Bun('White bun', 150.0)
        # Устанавливаем первую булку
        burger.set_buns(bun1)
        # Проверяем, что текущая булка равна bun1
        assert burger.bun == bun1
        # Устанавливаем вторую булку
        burger.set_buns(bun2)
        # Проверяем, что текущая булка равна bun2
        assert burger.bun == bun2

    """ Тест на добавление ингредиента """
    def test_add_ingredient(self):
        # Создаем экземпляр класса Burger
        burger = Burger()
        # Создаем mock объект для класса Ingredient
        mock_ingredient = Mock()
        # Устанавливаем возвращаемые значения для методов объекта mock
        mock_ingredient.get_name.return_value = 'Мини-салат Экзо-Плантаго'
        mock_ingredient.get_price.return_value = 9.0
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        # Вызываем метод add_ingredient() класса Burger и передаем в него mock объект
        burger.add_ingredient(mock_ingredient)
        # Проверяем, что значения, полученные из mock объекта, соответствуют ожидаемым значениям в классе Burger
        assert burger.ingredients[0].get_price() == 9.0
        assert burger.ingredients[0].get_name() == 'Мини-салат Экзо-Плантаго'
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

    """ Тест на удаление ингредиента """
    def test_remove_ingredient(self):
        # Создание экземпляра класса Burger
        burger = Burger()
        # Создание объекта-заглушки (Mock) для ингредиента
        mock_ingredient = Mock()
        # Добавляем заглушки ингредиента в бургер
        burger.add_ingredient(mock_ingredient)
        # Удаляем ингредиент на позиции 0 (первый ингредиент)
        burger.remove_ingredient(0)
        # Проверяем, что список ингредиентов в бургере пустой
        assert len(burger.ingredients) == 0

    """ Тест на перемещение ингредиента """
    def test_move_ingredient(self, cooked_burger_fixture):
        # Получаем первый и второй ингредиенты перед перемещением
        first_ingredient = cooked_burger_fixture.ingredients[0]
        second_ingredient = cooked_burger_fixture.ingredients[1]
        # Перемещаем ингредиенты
        cooked_burger_fixture.move_ingredient(0, 1)
        # Проверяем, что первый ингредиент стал вторым после перемещения
        assert first_ingredient == cooked_burger_fixture.ingredients[1]
        # Проверяем, что второй ингредиент стал первым после перемещения
        assert second_ingredient == cooked_burger_fixture.ingredients[0]

    """ Тест на получение цены """
    def test_get_price(self):
        # Создаем объекты бургера и базы данных
        burger = Burger()
        database = Database()
        # Устанавливаем булки, добавляем ингредиенты
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        # Проверяем, что цена бургера равна 400.0
        assert burger.get_price() == 400.0

    """ Тест на получение чека """
    def test_get_receipt(self):
        # Создаем объекты бургера и базы данных
        burger = Burger()
        database = Database()
        # Устанавливаем булки, добавляем ингредиенты
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        # Ожидаемый чек
        expected_receipt = "(==== black bun ====)\n"
        expected_receipt += "= sauce hot sauce =\n"
        expected_receipt += "= filling cutlet =\n"
        expected_receipt += "(==== black bun ====)\n\n"
        expected_receipt += "Price: 400"
        # Проверяем, что полученный чек равен ожидаемому чеку
        assert expected_receipt == burger.get_receipt()

