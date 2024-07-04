from praktikum.bun import Bun


def test_get_name():
    bulka = Bun('Rufl', 70)
    bulka.get_name()
    assert 'rtyh' == bulka.name


def test_get_price():
    bulka = Bun('Rufl', 70)
    bulka.get_price()
    assert 70 == bulka.price
