import pytest
from unittest.mock import Mock

import data.mock_variables as mock_var
from praktikum.database import Database
from praktikum.ingredient_types import *


class TestDatabase:
    @pytest.mark.parametrize("expected_buns", [("black bun", 100), ("white bun", 200), ("red bun", 300)])
    def test_available_buns(self, expected_buns):
        db = Database()
        expected_name, expected_price = expected_buns
        buns = db.available_buns()
        assert any(bun.name == expected_name and bun.price == expected_price for bun in buns)

    @pytest.mark.parametrize("expected_type, expected_name, expected_price", [
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    ])
    def test_available_ingredients(self, expected_type, expected_name, expected_price):
        db = Database()
        ingredients = db.available_ingredients()
        assert any(
            ingredient.type == expected_type and
            ingredient.name == expected_name and
            ingredient.price == expected_price
            for ingredient in ingredients
        )

    def test_mock_available_buns(self):
        db = Database()
        mock_db = Mock()
        mock_db.available_buns.return_value = mock_var.mock_db_bun
        db.available_buns = mock_db.available_buns
        assert db.available_buns() == ["Флюоресцентная булка R2-D3", "Краторная булка N-200i"]

    def test_mock_available_ingredients(self):
        db = Database()
        mock_db = Mock()
        mock_db.available_ingredients.return_value = mock_var.mock_db_ingredient
        db.available_ingredients = mock_db.available_ingredients
        assert db.available_ingredients() == ["Мясо бессмертных моллюсков Protostomia", "Сыр с астероидной плесенью"]
