import pytest

from burger import Burger


@pytest.fixture
def cosmic_burger():
    return Burger()