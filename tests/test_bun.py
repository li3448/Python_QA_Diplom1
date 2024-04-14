import allure
from praktikum.bun import Bun
from data import Data


class TestBun:

    @allure.title('Проверка создания булочки')
    @allure.description('Проверяем, что возможно создать булочку с именем и ценой')
    def test_create_bun_actual_name_and_price_successful(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)

        assert bun.name == 'Марсианский хлебушек' and bun.price == 1234.55

    @allure.title('Проверка получения имени булочки')
    @allure.description('Проверяем, что возможно получить имя булочки методом get_name')
    def test_get_name_successful(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)

        assert bun.get_name() == 'Марсианский хлебушек'

    @allure.title('Проверка получения цены булочки')
    @allure.description('Проверяем, что возможно получить цену булочки методом get_price')
    def test_get_price_successful(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)

        assert bun.get_price() == 1234.55
