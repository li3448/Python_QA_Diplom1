from burger import Burger
from bun import Bun


class TestBurger:
    def test_set_buns_bun_added_successfully(self):
        my_bun = Bun("булочка с кунжутом", 100)
        my_burger = Burger()
        my_burger.set_buns(my_bun)
        assert my_burger.get_price() == 200

