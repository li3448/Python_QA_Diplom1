from unittest.mock import patch, Mock
import pytest
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from database import Database

class TestBun:

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_get_name(self, index):
        database = Database()
        bun_name = database.buns[index].get_name()
        bun_price = database.buns[index].get_price()

        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name


    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_get_price(self, index):
        database = Database()
        bun_name = database.buns[index].get_name()
        bun_price = database.buns[index].get_price()

        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price

class TestBurger:
    @patch('Diplom_1.bun.Bun')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        database = Database()
        mock_bun = mock_bun.return_value
        mock_bun.get_name.return_value = database.ingredients[0].get_name()
        mock_bun.get_price.return_value = database.ingredients[0].get_price()

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    @patch('Diplom_1.ingredient.Ingredient')
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_add_ingredient(self, mock_ingredient, index):
        burger = Burger()
        database = Database()

        database_ingredient = database.ingredients

        mock_ingredient = mock_ingredient.return_value
        mock_ingredient.get_type.return_value = database_ingredient[index].get_type()
        mock_ingredient.get_name.return_value = database_ingredient[index].get_name()
        mock_ingredient.get_price.return_value = database_ingredient[index].get_price()

        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0].get_type() == database_ingredient[index].get_type()
        assert burger.ingredients[0].get_name() == database_ingredient[index].get_name()
        assert burger.ingredients[0].get_price() == database_ingredient[index].get_price()

    @patch('Diplom_1.ingredient.Ingredient')
    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        database = Database()
        database_ingredient = database.ingredients

        mock_ingredient = mock_ingredient.return_value
        mock_ingredient.get_type.return_value = database_ingredient[0].get_type()
        mock_ingredient.get_name.return_value = database_ingredient[0].get_name()
        mock_ingredient.get_price.return_value = database_ingredient[0].get_price()

        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    @patch('Diplom_1.ingredient.Ingredient')
    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        database = Database()
        database_ingredient = database.ingredients

        mock_ingredient = mock_ingredient.return_value
        mock_ingredient.get_type.return_value = database_ingredient[0].get_type()
        mock_ingredient.get_name.return_value = database_ingredient[0].get_name()
        mock_ingredient.get_price.return_value = database_ingredient[0].get_price()

        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 0)

        assert burger.ingredients[0].get_type() == database_ingredient[0].get_type()
        assert burger.ingredients[0].get_name() == database_ingredient[0].get_name()
        assert burger.ingredients[0].get_price() == database_ingredient[0].get_price()


    @patch('Diplom_1.ingredient.Ingredient')
    @patch('Diplom_1.bun.Bun')
    @pytest.mark.parametrize('index_bun, index_sause, index_filling',
                             [
                                 (0, 0, 3)
                             ])
    def test_get_price(self, mock_ingredient, mock_bun, index_bun, index_sause, index_filling):
        burger = Burger()
        database = Database()
        database_ingredient = database.ingredients

        mock_bun = mock_bun.return_value
        mock_bun.get_name.return_value = database.buns[index_bun].get_name()
        mock_bun.get_price.return_value = database.buns[index_bun].get_price()

        burger.set_buns(mock_bun)


        mock_ingredient = mock_ingredient.return_value
        mock_ingredient.get_type.return_value = database_ingredient[index_sause].get_type()
        mock_ingredient.get_name.return_value = database_ingredient[index_sause].get_name()
        mock_ingredient.get_price.return_value = database_ingredient[index_sause].get_price()

        burger.add_ingredient(mock_ingredient)

        mock_ingredient = mock_ingredient.return_value
        mock_ingredient.get_type.return_value = database_ingredient[index_filling].get_type()
        mock_ingredient.get_name.return_value = database_ingredient[index_filling].get_name()
        mock_ingredient.get_price.return_value = database_ingredient[index_filling].get_price()

        burger.add_ingredient(mock_ingredient)


        price = burger.get_price()

        assert price == 400

    @patch('Diplom_1.ingredient.Ingredient')
    @patch('Diplom_1.bun.Bun')
    @pytest.mark.parametrize('index_bun, index_sauce, index_filling',
                             [
                                 (0, 0, 4)
                             ])
    def test_get_receipt(self, mock_ingredient, mock_bun,  index_bun, index_sauce, index_filling):
        burger = Burger()
        database = Database()
        database_ingredient = database.ingredients

        mock_bun = mock_bun.return_value
        mock_bun.get_name.return_value = database.buns[index_bun].get_name()
        mock_bun.get_price.return_value = database.buns[index_bun].get_price()

        burger.set_buns(mock_bun)

        mock_ingredient = mock_ingredient.return_value
        mock_ingredient.get_type.return_value = database_ingredient[index_sauce].get_type()
        mock_ingredient.get_name.return_value = database_ingredient[index_sauce].get_name()
        mock_ingredient.get_price.return_value = database_ingredient[index_sauce].get_price()

        burger.add_ingredient(mock_ingredient)

        mock_ingredient = mock_ingredient.return_value
        mock_ingredient.get_type.return_value = database_ingredient[index_filling].get_type()
        mock_ingredient.get_name.return_value = database_ingredient[index_filling].get_name()
        mock_ingredient.get_price.return_value = database_ingredient[index_filling].get_price()

        burger.add_ingredient(mock_ingredient)


        receipt = burger.get_receipt()

        print(receipt)

        assert receipt.count(mock_bun.get_name()) == 2
        assert "sauce" in receipt
        assert "hot sauce" in receipt
        assert "filling" in receipt
        assert "dinosaur" in receipt
        assert "Price: 500" in receipt



class TestIngredient:

    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_get_price(self, index):
        database = Database()
        type = database.ingredients[index].get_type()
        name = database.ingredients[index].get_name()
        price = database.ingredients[index].get_price()

        ingredients = Ingredient(type, name, price)

        assert ingredients.get_price() == price

    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_get_name(self, index):
        database = Database()
        type = database.ingredients[index].get_type()
        name = database.ingredients[index].get_name()
        price = database.ingredients[index].get_price()

        ingredients = Ingredient(type, name, price)

        assert ingredients.get_name() == name

    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_get_type(self, index):
        database = Database()
        type = database.ingredients[index].get_type()
        name = database.ingredients[index].get_name()
        price = database.ingredients[index].get_price()

        ingredients = Ingredient(type, name, price)

        assert ingredients.get_type() == type


class TestDatabase:

    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_available_buns(self, index):
        database = Database()
        bun_list = database.available_buns()
        bun_name = database.buns[index].name

        assert bun_name == bun_list[index].name


    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_available_ingredients(self, index):
        database = Database()
        ingredients_list = database.available_ingredients()
        ingredient_name = database.ingredients[index].name

        assert ingredient_name == ingredients_list[index].name












