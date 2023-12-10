from dataclasses import dataclass
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@dataclass
class Ingredient:
    type: str
    name: str
    price: float


filling = Ingredient(
    type=INGREDIENT_TYPE_FILLING,
    name='Cutlet',
    price=200)

sauce = Ingredient(
    type=INGREDIENT_TYPE_SAUCE,
    name='Hot sauce',
    price=30.4)