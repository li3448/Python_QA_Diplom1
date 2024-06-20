from unittest.mock import Mock
import pytest
from burger import Burger


@pytest.fixture
def cosmic_burger():
    return Burger()


@pytest.fixture
def mock_bun():
    return Mock()


@pytest.fixture
def mock_ingridient():
    return Mock()


@pytest.fixture
def mock_bun_price():
    return Mock()
