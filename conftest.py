import pytest
from unittest.mock import Mock

from .data import (DataBun as DB,
                   DataIngredient as DI)
from .praktikum.bun import Bun
from .praktikum.burger import Burger
from .praktikum.ingredient import Ingredient


@pytest.fixture()
def get_bun():
    """Возвращает экземпляр класса Bun."""
    bun = Bun(DB.BUN_NAME, DB.BUN_PRICE)
    return bun


@pytest.fixture()
def get_ingredient():
    """Возвращает экземпляр класса Ingredient."""
    ingredient = Ingredient(
        DI.ING_TYPE,
        DI.ING_NAME,
        DI.ING_PRICE1)
    return ingredient


@pytest.fixture()
def get_burger():
    """Возвращает экземпляр класса Burger."""
    burger = Burger()
    return burger


@pytest.fixture()
def get_bun_mock_data():
    """Возвращает замокированный экземпляр класса Bun."""
    mock_bun = Mock()
    mock_bun.name = mock_bun.get_name.return_value = DB.BUN_NAME
    mock_bun.price = mock_bun.get_price.return_value = DB.BUN_PRICE
    return mock_bun


@pytest.fixture()
def get_ing_mock_data():
    """Возвращает список замокированных экземпляров класса Ingredient."""
    get_burger.ingredients = []
    for i in range(len(DI.ING_NAME_LIST)):
        mock_ing = Mock()
        mock_ing.price = mock_ing.get_price.return_value = DI.ING_PRICE_LIST[i]
        mock_ing.name = mock_ing.get_name.return_value = DI.ING_NAME_LIST[i]
        mock_ing.type = mock_ing.get_type.return_value = DI.ING_TYPE_LIST[i]
        get_burger.ingredients.append(mock_ing)
    return get_burger.ingredients


@pytest.fixture()
def get_price_burger_mock(get_bun_mock_data, get_ing_mock_data):
    """
    Возвращает стоимость бургера,
    рассчитанную на замокированных экземпярах
    классов Bun и Ingredient.
    """
    get_burger.ingredients = get_ing_mock_data
    get_burger.bun = get_bun_mock_data
    current_price = get_burger.bun.price * 2
    for ingredient in get_burger.ingredients:
        current_price += ingredient.price
    return current_price
