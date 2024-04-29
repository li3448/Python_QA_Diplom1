from unittest.mock import patch, Mock
import allure
import pytest
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from database import Database

class TestBun:
    @allure.title('Проверка возврата имени из аргумента конструктора класса name, класса Bun.')
    @allure.description('Проверяем, что метод get_name, возвращает имя, полученное из объекта класса Bun, значение которого,'
                        'заимствуется из базы данных')
    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_get_name(self, index):
        database = Database()
        bun_name = database.buns[index].get_name()
        bun_price = database.buns[index].get_price()

        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name

    @allure.title('Проверка возврата цены из аргумента конструктора класса price, класса Bun.')
    @allure.description('Проверяем, что метод get_price, возвращает цену, полученную из объекта класса Bun, значение которого,'
                        'заимствуется из базы данных')
    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_get_price(self, index):
        database = Database()
        bun_name = database.buns[index].get_name()
        bun_price = database.buns[index].get_price()

        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price

class TestBurger:
    @allure.title('Проверка назначения переденного объекта класса в качестве аргумента bun')
    @allure.description(
        'Проверяем, что метод set_buns, назначает переданный ему объект класса в качестве'
        'аргумента метода bun')
    @patch('Diplom_1.bun.Bun')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        database = Database()
        mock_bun = mock_bun.return_value
        mock_bun.get_name.return_value = database.ingredients[0].get_name()
        mock_bun.get_price.return_value = database.ingredients[0].get_price()

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    @allure.title('Проверка добавления значений переданного объекта класса Ingredient в список конструктора класса ingredients')
    @allure.description(
        'Проверяем, что метод add_ingredient, после передачи в него объекта класса Ingredient, добавляет значения класса'
        'в список конструктора класса ingredients')
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

    @allure.title('Проверка удаления элемента из списка ingredients, конструктора класса ingredients')
    @allure.description(
        'Проверяем, что метод remove_ingredient после передачи в него идекса элемента списка ingredients, конструктора класса ingredients'
        'удаляет данный элемент из списка')
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

    @allure.title('Проверка замены элемента из списка ingredients, конструктора класса ingredient, на новый элемент')
    @allure.description(
        'Проверяем, что метод move_ingredient после передачи в него идекса элемента списка ingredients, конструктора класса ingredients'
        'и нового индекса, для указания, на какое место в списке, будет перемещен элемент списка, соответствующий переданному значению imdex,'
        'происходит извлечение из списка элемента, который соответствует значению index и установка его на новое место в списке,'
        'которое соответствует значению new_index')
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


    @allure.title('Проверка, получения суммарной стоимости буогера, которая состоит из стоимости булки, '
                  'умноженной на 2 и стомости выбранных ингридиентов')
    @allure.description(
        'Проверяем, что метод get_price, возвращает суммарную стоимость бургера, которая была сформирована,'
        'из полученной стоимости булки, умноженной на 2 и полученной стоимости ингредиентов, добавленных в список ingredients'
        'констуктора класса Ingredient')
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

    @allure.title('Проверка, получения чека, состоящего из наименования ингредиентов бургера и общей суммы')
    @allure.description(
        'Проверяем, что метод get_receipt возвращает, чек с указаением в заголовке имени булки, полученной из аргумента bun,'
        'конструктора класса, типа и имени ингредиентов, полученных из списка ingredients конструктора класса,'
        'а также суммарной стоимости бургера, полученной в спомощью метода get_price')
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

    @allure.title('Проверка, получения цены, из переденного в конструктор класса Ingredient, элемента из базы данных')
    @allure.description(
        'Проверяем, что метод get_price возвращает, цену из элемента, который был передан в конструктор класса Ingredient из списка ingredients')
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_get_price(self, index):
        database = Database()
        type = database.ingredients[index].get_type()
        name = database.ingredients[index].get_name()
        price = database.ingredients[index].get_price()

        ingredients = Ingredient(type, name, price)

        assert ingredients.get_price() == price

    @allure.title('Проверка, получения имени, из переденного в конструктор класса Ingredient, элемента из базы данных')
    @allure.description(
        'Проверяем, что метод get_name возвращает, имя из элемента, который был передан в конструктор класса Ingredient из списка ingredients')
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_get_name(self, index):
        database = Database()
        type = database.ingredients[index].get_type()
        name = database.ingredients[index].get_name()
        price = database.ingredients[index].get_price()

        ingredients = Ingredient(type, name, price)

        assert ingredients.get_name() == name

    @allure.title('Проверка, получения типа ингредиета, из переденного в конструктор класса Ingredient, элемента из базы данных')
    @allure.description(
        'Проверяем, что метод get_type возвращает, тип ингредиента из элемента, который был передан в конструктор класса Ingredient из списка ingredients')
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5])
    def test_get_type(self, index):
        database = Database()
        type = database.ingredients[index].get_type()
        name = database.ingredients[index].get_name()
        price = database.ingredients[index].get_price()

        ingredients = Ingredient(type, name, price)

        assert ingredients.get_type() == type


class TestDatabase:
    @allure.title('Проверка, получения списка buns с элиментами bun , конструктора класса Database')
    @allure.description(
        'Проверяем, что метод available_buns возвращает, список, содержащий элементы bun')
    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_available_buns(self, index):
        database = Database()
        bun_list = database.available_buns()
        bun_name = database.buns[index].name

        assert bun_name == bun_list[index].name

    @allure.title('Проверка, получения списка buns с элиментами bun , конструктора класса Database')
    @allure.description(
        'Проверяем, что метод available_ingredients возвращает, список, содержащий элементы ingredient')
    @pytest.mark.parametrize('index', [0, 1, 2])
    def test_available_ingredients(self, index):
        database = Database()
        ingredients_list = database.available_ingredients()
        ingredient_name = database.ingredients[index].name

        assert ingredient_name == ingredients_list[index].name













