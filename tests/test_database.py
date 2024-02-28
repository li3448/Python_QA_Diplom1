from unittest.mock import Mock

from ..data import DataBun as DB
from ..praktikum.database import Database


class TestDatabase:

    def test_available_buns_success(self):
        database = Database()
        mock_bun_lst = []
        for i in range(len(DB.BUN_NAME_LIST)):
            mock = Mock()
            mock.name = DB.BUN_NAME_LIST[i]
            mock.price = DB.BUN_PRICE_LIST[i]
            mock_bun_lst.append(mock)
        for i in range(len(mock_bun_lst)):
            assert mock_bun_lst[i].name == database.available_buns()[i].name
            assert mock_bun_lst[i].price == database.available_buns()[i].price

    def test_available_ingredients_success(self, get_ing_mock_data):
        database = Database()
        for i in range(len(get_ing_mock_data)):
            assert get_ing_mock_data[i].name == database.available_ingredients()[i].name
            assert get_ing_mock_data[i].price == database.available_ingredients()[i].price
            assert get_ing_mock_data[i].type == database.available_ingredients()[i].type
