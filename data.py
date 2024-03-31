import random
from typing import List

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def generator_ingredients(count=0) -> List[Ingredient]:
    """
    генератор списка ингредиентов соответствующего класса
    count = 0 по умолчанию для случая бургера без ингредиентов
    """
    ingredients = []
    for index in range(1, count + 1):
        type = random.choice(['SAUCE', 'FILLING'])
        name = f'test_name_ingredient_{index}'
        price = 5 * index
        ingredients.append(Ingredient(ingredient_type=type, name=name, price=price))
    return ingredients
