import pytest

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from praktikum.database import Database


class TestDatabase:
   
    )
    def test_available_buns_bun_in_list(self, bun_name, bun_price, index):
        database = Database()
        buns_list = database.available_buns()

        assert (
                buns_list[index].get_name() == bun_name and
                buns_list[index].get_price() == bun_price
        )

