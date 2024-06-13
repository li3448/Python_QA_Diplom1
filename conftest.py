from unittest.mock import Mock
import pytest


@pytest.fixture
def mock_bun():
    return Mock()


@pytest.fixture
def mock_ingredient():
    return Mock()
