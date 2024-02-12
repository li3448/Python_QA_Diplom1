from tests.data import TestData
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger


class TestBurger:
    """
    Тесты создания объекта класса Burger
    """
    def test_burger_contain(self):
        burger = Burger()
        assert burger.bun is None, f"Атрибут bun экземпляра класса Burger не пустой, содержит {burger.bun}"
        assert burger.ingredients == [], f"Атрибут ingredients экземпляра класса Burger не пустой, содержит {burger.ingredients}"

    """
    Тесты методов класса Burger
    """
    """Проверка методом set_buns проверим имя булочки бургера"""
    def test_set_buns_there_is_name(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.name = TestData.BUN_NAME
        burger.set_buns(bun=mock_bun)
        assert burger.bun.name == TestData.BUN_NAME

    """Проверка методом set_buns проверим цену булочки бургера"""
    def test_set_buns_there_is_price(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.price = TestData.BUN_PRICE
        burger.set_buns(mock_bun)
        assert burger.bun.price == TestData.BUN_PRICE

    """Метод add_ingredient добавление ингредиента в бургер"""
    def test_add_ingredient(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        pass

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0
