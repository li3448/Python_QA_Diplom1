class Data:
    """ data bun """
    BUN_NAME = 'Флюоресцентная булка R2-D3', 'Краторная булка N-200i'
    BUN_PRICE = 988, 1255

    """ data ingredient """
    ING_NAME = 'Spicy-X'
    ING_TYPE = 'Соусы'
    ING_PRICE = 90

    """ data for test_burger """
    EXPECTED_RESULT = "(==== Флюоресцентная булка R2-D3 ====)\n" \
                      "= соусы Spicy-X =\n" \
                      "(==== Флюоресцентная булка R2-D3 ====)\n" \
                      "\n" \
                      "Price: 2066"
