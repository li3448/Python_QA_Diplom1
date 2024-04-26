from ingredient_types import IngredientTypeEnum


class TestData:

    BUN = ('bun name 1', 1)
    ANOTHER_BUN = ('bun name 2', 2)

    INGREDIENT = (
        IngredientTypeEnum.INGREDIENT_TYPE_FILLING,
        'name',
        1
    )

    INGREDIENTS_LIST = [
        {
            'type': IngredientTypeEnum.INGREDIENT_TYPE_FILLING,
            'name': 'ingredient name 1',
            'price': 1,
        },
        {
            'type': IngredientTypeEnum.INGREDIENT_TYPE_SAUCE,
            'name': 'ingredient name 2',
            'price': 2,
        },
    ]