
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
#Проверка создания ингредиента
    def test_ingredient_creation(self, sauce):
        assert sauce.type == INGREDIENT_TYPE_SAUCE
        assert sauce.name == "hot sauce"
        assert sauce.price == 100

    @pytest.mark.parametrize(
        'ingr_type',
        [
            'sauce', 'filling'
        ]
    )
    #Получаем цену ингредиента
    def test_get_ingredient_price(self, request, ingr_type):
        ingredient = request.getfixturevalue(ingr_type)
        assert ingredient.get_price() == 100

    @pytest.mark.parametrize(
        'ingr_type, result',
        [
            ('sauce', "hot sauce"),
            ('filling', "cutlet")
        ]
    )
    #Получаем название ингредиента
    def test_get_ingredient_name(self, request, ingr_type, result):
        ingredient = request.getfixturevalue(ingr_type)
        assert ingredient.get_name() == result

    @pytest.mark.parametrize(
        'ingr_type, result',
        [
            ('sauce', INGREDIENT_TYPE_SAUCE),
            ('filling', INGREDIENT_TYPE_FILLING)
        ]
    )
    #Получаем тип ингредиента
    def test_get_ingredient_type(self, request, ingr_type, result):
        ingredient = request.getfixturevalue(ingr_type)
        assert ingredient.get_type() == result
