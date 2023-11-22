import sys, os

python_path = os.path.join(os.getcwd())
sys.path.append(python_path)
os.environ["PYTHONPATH"] = python_path

from praktikum.bun import Bun

class TestBun:
    def test_bun_name(self):
        buns = Bun('Tasty Bun', 12)
        assert buns.get_name() == 'Tasty Bun'

    def test_bun_price(self):
        buns = Bun('Tasty Bun', 10.0)
        assert buns.get_price() == 10.0

    def test_bun_price_wrong_format(self):
        buns = Bun('Tasty Bun', 'Tasty Bun2')
        assert type(buns.get_price()) is not float

    def test_bun_price_correct_format(self):
        buns = Bun('Tasty Bun', 10.0)
        assert type(buns.get_price()) is float