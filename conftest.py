import pytest
from praktikum.bun import Bun


@pytest.fixture(scope='function')
def bun():
    bun = Bun('Крейзи_Булка', 999)
    return bun
