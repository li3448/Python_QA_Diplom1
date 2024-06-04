from data import Data


# Проверки класса Burger с мокирование Bun и Ingredient
class TestBurger:
    def test_get_price_burger_return_return_sum(self, burger_instance, mock_bun_get_price, mock_ingredient_get_price):
        burger_instance.set_buns(mock_bun_get_price)
        burger_instance.add_ingredient(mock_ingredient_get_price)

        result_mock = mock_bun_get_price.get_price() * 2 + mock_ingredient_get_price.get_price()

        assert burger_instance.get_price() == result_mock

    def test_get_receipt_burger_return_string(self, burger_instance, mock_bun_get_price, mock_bun_get_name,
                                              mock_ingredient_get_price, mock_ingredient_get_name_and_get_type):
        burger_instance.set_buns(mock_bun_get_price)
        burger_instance.add_ingredient(mock_ingredient_get_price)

        assert burger_instance.get_receipt() == Data.RESULT_GET_RECEIPT_FROM_MOCK
