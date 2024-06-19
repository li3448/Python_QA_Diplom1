import random
import time

from faker import Faker

from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE


def generate_name():
    data = Faker()

    name = f"{data.first_name()}{(str(round(time.time())))}"

    return name


def generate_price():
    price = random.uniform(0, 100)

    return price


def generate_bun():
    name = generate_name()

    price = generate_price()

    bun = Bun(name=name, price=price)

    return bun


def generate_burger():
    burger = Burger()

    bun = generate_bun()

    burger.set_buns(bun)

    return burger


def generate_ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name=generate_name(), price=generate_price()):
    ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)

    return ingredient
