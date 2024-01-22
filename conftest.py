import pytest

from praktikum.burger import Burger


@pytest.fixture
def burger():
    """Фикстура создает объект бургера"""
    burger = Burger()
    return burger
