import random


class DataBun:
    name = ['Флюоресцентная', 'Краторная']
    price = [988, 1255]

    @classmethod
    def get_data_bun(cls):
        return random.choice(cls.name), random.choice(cls.price)


class DataIngredient:
    name = ['Spicy-X', 'Space Sauce']
    price = [90, 80]
    type = ['sauce', 'filling']

    @classmethod
    def get_data_ingredient(cls):
        return random.choice(cls.name), random.choice(cls.price), random.choice(cls.type)







