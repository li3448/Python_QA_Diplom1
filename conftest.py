from unittest.mock import Mock
import pytest
from tests.data import MockBun


@pytest.fixture(scope='function')
def mok_bun():
    bun = Mock()
    bun.get_name.return_value = MockBun.NAME
    bun.get_price.return_value = MockBun.PRICE

    return bun
