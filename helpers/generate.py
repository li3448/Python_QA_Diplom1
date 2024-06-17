import random
import time

from faker import Faker

from bun import Bun
from burger import Burger


def generate_name():
    data = Faker()
    login = f"{data.first_name()}{(str(round(time.time())))}"
    return login


def generate_price():
    return random.uniform(0, 100)


def generate_burger():
    burger = Burger()
    name = generate_name()
    price = generate_price()

    bun = Bun(name=name, price=price)
    burger.set_buns(bun)
    return burger
