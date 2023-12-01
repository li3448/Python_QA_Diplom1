from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from unittest.mock import Mock


class TestData:
    bun = Bun('Сэндвич с вогонской плесенью', 1500)
    ingredient = Ingredient('SAUCE', 'Соус Экстратеррестрис', 3000)
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Мирфакианская булькающая булка'
    mock_bun.get_price.return_value = 1000
    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.get_name.return_value = 'Соус Галактическая Погремушка'
    mock_ingredient_sauce.get_price.return_value = 3000
    mock_ingredient_sauce.get_type.return_value = 'SAUCE'
    mock_ingredient_filling = Mock()
    mock_ingredient_filling.get_name.return_value = 'Гамма-нейтронная котлета на кости Тау Кита'
    mock_ingredient_filling.get_price.return_value = 5000
    mock_ingredient_filling.get_type.return_value = 'FILLING'
