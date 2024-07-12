class TestBurger:

#Проверка создания пустого бургера без булочки и ингридиентов
    def test_create_burger(self):
        burger = Burger()
        assert burger.bun is None
#Добавление булочки
    def test_add_bun_burger(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
#Добавление ингредиентов
    def test_add_ingredient_burger(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert mock_sauce in burger.ingredients
#Удаление ингредиентов
    def test_delete_ingredient_burger(self, full_burger):
        full_burger.remove_ingredient(0)
        assert len(full_burger.ingredients) == 1
#Перетаскивание ингредиентов
    def test_move_ingredient_burger(self, full_burger, mock_sauce):
        full_burger.move_ingredient(0, 1)
        assert full_burger.ingredients[1] == mock_sauce
#Получение цены булочки с ингредиентами
def test_get_full_price_burger(self, full_burger, mock_bun, mock_sauce, mock_filling):
    expected_price = mock_bun.get_price.return_value + mock_sauce.get_price.return_value + mock_filling.get_price.return_value
    assert full_burger.get_price() == expected_price
#Получение чека
    def test_get_receipt_burger(self, full_burger):
        assert full_burger.get_receipt() == ('(==== white bun ====)\n'
                                             '= sauce sour cream =\n'
                                             '= filling dinosaur =\n'
                                             '(==== white bun ====)\n'
                                             '\n'
                                             'Price: 800')