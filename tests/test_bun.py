import pytest

from praktikum.bun import Bun

""" Тесты для класса Bun """
class TestBun:
    """ Тест на добавление наименования булки """
    @pytest.mark.parametrize('name',
                             ["Бриошь",
                              "Чиабатта",
                              "Кайзер-ролл",
                              "Английский маффин"
                              ])
    def test_get_name(self, name):
        # Создание экземпляра класса Bun с определенными значениями name
        bun = Bun(name, 22.0)
        # Проверка, что полученное значение имени соответствует ожидаемому значению
        assert bun.get_name() == name

    """ Тест на добавление цены булки """
    @pytest.mark.parametrize('price',
                             [15.0,
                              0.0,
                              1.7976931348623157e+308,
                              2.2250738585072014e-308])
    def test_get_price(self, price):
        # Создание экземпляра класса Bun с определенными значениями price
        bun = Bun("Крендель", price)
        # Проверка, что полученное значение цены соответствует ожидаемому значению
        assert bun.get_price() == price
