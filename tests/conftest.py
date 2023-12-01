import pytest
from data import TestData
from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture
def burger():
    burger = Burger()
    burger.set_buns(TestData.mock_bun)
    yield burger

@pytest.fixture
def database():
    return Database()