import pytest
from bun import Bun


@pytest.fixture(params=[
    ('Baguette 123', 100.99),
    ('Бриошь', 150)
])
def bun(request):
    name, price = request.param
    return Bun(name, price)
