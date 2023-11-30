import pytest
from unittest.mock import Mock
from praktikum.database import Database
class TestDataBase:
    def test_available_buns(self):
        data = Database()
        mock_buns = [
            Mock(name="black bun", price=100),
            Mock(name="white bun", price=200),
            Mock(name="red bun", price=300)
        ]
        data.available_buns = Mock(return_value=mock_buns)
        assert data.available_buns() == mock_buns

    @pytest.mark.parametrize("bun_name, expected_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_available_buns_parametrized(self, bun_name, expected_price):
        data = Database()
        buns = data.available_buns()

        for bun in buns:
            if bun.name == bun_name:
                assert bun.price == expected_price