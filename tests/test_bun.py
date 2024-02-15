import pytest

from tests.data import TestData
from praktikum.bun import Bun


class TestBun:
    """
    Тесты создание объекта класса Bun
    """
    """Тест проверка имени булочки для бургера"""
    @pytest.mark.parametrize(
        "name,price", [("Имя", 120.7), ("Имя1", 120.7), ("имя", 120.7), ("name", 120.7), ("", 120.7)])
    def test_name_of_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name, f"Ожидалась имя булочки {name}, но получено {bun.name}"

    """Тест проверка цены булочки для бургера"""
    @pytest.mark.parametrize(
        "name,price", [("Имя", 120.7), ("Имя", 120), ("Имя", 12000000), ("Имя", 0), ("Имя", -1)])
    def test_price_of_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.price == price, f"Ожидалась цена булочки {price}, но получено {bun.price}"

    """
    Тесты методов класса Bun
    """
    """Тест метод get_name возвращает имя булочки"""
    @pytest.mark.parametrize(
        "name", ["Имя", "Имя1", "имя", "name", "", None])
    def test_get_name_true_name(self, name):
        bun = Bun(name, TestData.BUN_PRICE)
        assert bun.get_name() == name, f"Ожидалась имя булочки {name}, получена {bun.get_name()}"

    """Тест метод get_name возвращает тип данных str"""
    def test_get_name_return_str(self):
        bun = Bun(TestData.BUN_NAME, TestData.BUN_PRICE)
        name_result = bun.get_name()
        assert isinstance(name_result, str), f"Ожидалась 'str', но получено {type(name_result)}"

    """Тест успешное получение цены созданной булочки для бургера метод get_price"""
    @pytest.mark.parametrize(
        "price", [120.7, 120, 120000000000000, 0, -1])
    def test_get_price_true_price(self, price):
        bun = Bun(TestData.BUN_NAME, price)
        assert bun.get_price() == price, f"Ожидалась цена {price}, получена {bun.get_price()}"

    """Тест возвращает тип данных float метод get_price"""
    def test_get_price_true_return_float(self):
        bun = Bun(TestData.BUN_NAME, TestData.BUN_PRICE)
        name_result = bun.get_price()
        assert isinstance(name_result, float), f"Ожидалась 'float', но получено {type(name_result)}"