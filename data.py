class Values:

    BUN_NAME = 'Булка без начинки'
    BUN_PRICE = 100
    BUN_PRICES = 100, 1, 0, 999999

    INGREDIENT_NAME = 'сливки'
    INGREDIENT_PRICE = 200
    INGREDIENT_TYPE = 'соус'


    EXPEXTED_RECEIPT = "(==== Булка без начинки ====)\n" \
                       "= соус сливки =\n" \
                       "= соус сливки =\n" \
                       "(==== Булка без начинки ====)\n" \
                       "\n" \
                       "Price: 600"
