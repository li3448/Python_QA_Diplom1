import pytest

from praktikum.bun import Bun


@pytest.fixture(scope='session')
def bun_create():
    res = Bun(name = 'Сливочный', price= 2.5)
    return res