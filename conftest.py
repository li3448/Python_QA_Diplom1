import pytest

from unittest.mock import Mock
from data import MockSamples

@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_price.return_value = MockSamples.mock_bun_price
    mock_bun.get_name.return_value = MockSamples.mock_bun_name
    return mock_bun

@pytest.fixture(scope='function')
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_price.return_value = MockSamples.mock_sauce_price
    mock_sauce.get_name.return_value = MockSamples.mock_sauce_name
    mock_sauce.get_type.return_value = MockSamples.mock_sauce_type
    return mock_sauce

@pytest.fixture(scope='function')
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_price.return_value = MockSamples.mock_filling_price
    mock_filling.get_name.return_value = MockSamples.mock_filling_name
    mock_filling.get_type.return_value = MockSamples.mock_filling_type
    return mock_filling
