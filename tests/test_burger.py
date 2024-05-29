from unittest.mock import Mock


class TestBurger:

    def test_set_buns(self, file_o_fish):
        mock_bun = Mock()
        file_o_fish.set_buns(mock_bun)
        assert file_o_fish.bun == mock_bun

    def test_get_price(self, file_o_fish):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 1000
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 600
        file_o_fish.bun = mock_bun
        file_o_fish.ingredients = [mock_ingredient]
        assert file_o_fish.get_price() == 1000*2+600

    def test_add_ingredient(self, file_o_fish):
        mock_ingredient = Mock()
        file_o_fish.add_ingredient(mock_ingredient)
        assert file_o_fish.ingredients == [mock_ingredient]

    def test_remove_ingredient(self, file_o_fish):
        mock_ingredient = Mock()
        file_o_fish.add_ingredient(mock_ingredient)
        file_o_fish.remove_ingredient(0)
        assert file_o_fish.ingredients == []




