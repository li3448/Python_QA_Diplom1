import pytest

from praktikum.bun import Bun


@pytest.fixture(scope = 'function')
def bun_create():
    bun = Bun(name = 'Сливочный', price= 2.5)
    return bun