from random import choice, randrange
from string import ascii_uppercase


moc_bun_name = ''.join(choice(ascii_uppercase) for b in range(10))
moc_ingredient_name = ''.join(choice(ascii_uppercase) for i in range(10))
moc_bun_price = randrange(100, 1000)
moc_ingredient_price = randrange(100, 1000)