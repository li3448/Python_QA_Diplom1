class Data:
    BUN_NAME = 'Burger'
    BUN_PRICE = 269.9
    INGREDIENT_PRICE = 800
    INGREDIENTS_TYPE = 'Lite'
    INGREDIENT_NAME = 'Bread'

    RESULT_GET_RECEIPT_FROM_MOCK = (f'(==== {BUN_NAME} ====)'
                                    f'\n= {INGREDIENTS_TYPE.lower()} {INGREDIENT_NAME} ='
                                    f'\n(==== {BUN_NAME} ====)\n'
                                    f'\nPrice: {BUN_PRICE * 2 + INGREDIENT_PRICE}')
