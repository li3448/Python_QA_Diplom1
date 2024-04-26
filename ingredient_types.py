"""
Перечисление с типами ингредиентов.
SAUCE – соус
FILLING – начинка
"""
INGREDIENT_TYPE_SAUCE = 'SAUCE'
INGREDIENT_TYPE_FILLING = 'FILLING'

from enum import Enum, unique, StrEnum


@unique
class IngredientTypeEnum(StrEnum):
    INGREDIENT_TYPE_SAUCE = 'SAUCE'
    INGREDIENT_TYPE_FILLING = 'FILLING'

# IngredientTypeEnum.INGREDIENT_TYPE_FILLING
