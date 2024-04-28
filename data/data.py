from ingredient_types import IngredientTypeEnum


class TestData:

    BUNS_LIST = [
        ('bun name 1', 1),
        ('bun name 2', 2)
    ]

    INGREDIENTS_LIST: list[dict] = [
        {
            'type': IngredientTypeEnum.INGREDIENT_TYPE_FILLING,
            "name": 'ingredient name 1',
            'price': 1,
        },
        {
            'type': IngredientTypeEnum.INGREDIENT_TYPE_SAUCE,
            "name": 'ingredient name 2',
            'price': 2,
        },
    ]

    BURGERS_LIST: list[dict[str, list | dict]] = [
        {
            'ingredients': [],
            'bun': {
                'price': 0
            },
        },
        {
            'ingredients': [
                {
                    'type': IngredientTypeEnum.INGREDIENT_TYPE_SAUCE,
                    "name": 'sauce name 2',
                    'price': 2,
                },
            ],
            'bun': {
                'price': 0
            },
        },
        {
            'ingredients': [],
            'bun': {
                'name': 'bun name 1',
                'price': 10
            },
        },
        {
            'ingredients': [
                {
                    'type': IngredientTypeEnum.INGREDIENT_TYPE_FILLING,
                    "name": 'filling name 1',
                    'price': 125,
                },
            ],
            'bun': {
                'name': 'bun name 1',
                'price': 25
            },
        },
        {
            'ingredients': [
                {
                    'type': IngredientTypeEnum.INGREDIENT_TYPE_FILLING,
                    "name": 'filling name 1',
                    'price': 100,
                },
                {
                    'type': IngredientTypeEnum.INGREDIENT_TYPE_SAUCE,
                    "name": 'sauce name 2',
                    'price': 200,
                },
            ],
            'bun': {
                'name': 'bun name 123',
                'price': 1000
            },
        },
    ]