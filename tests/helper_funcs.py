from typing import Any
from unittest.mock import Mock
import re

from burger import Burger


class HelperFuncs:

    @staticmethod
    def create_burger_instance(
        attrs: dict[str, Any]
    ):
        bun = Mock()
        bun.name = attrs['bun'].get('name')
        bun.price = attrs['bun'].get('price')
        bun.get_price.return_value = attrs['bun'].get('price')
        bun.get_name.return_value = attrs['bun'].get('name')
        burger = Burger()
        burger.bun = bun
        burger.ingredients = []
        for i in attrs['ingredients']:
            elem = Mock()
            elem.name = i['name']
            elem.price = i['price']
            elem.type = i['type']
            elem.get_price.return_value = i.get('price')
            elem.get_name.return_value = i.get('name')
            elem.get_type.return_value = i.get('type')
            def __eq__(self, other):
                print('!!!!!!!!!!!!!!!!', self.name, other.name)
                return (
                    self.name == other.name and
                    self.price == other.price and
                    self.type == other.type
                )

            elem.__eq__ = __eq__
            burger.ingredients.append(elem)
        return burger

    @staticmethod
    def get_burger_price(item: dict):
        bun_price = item.get('bun').get('price')
        ingredient_price = sum(
            map(
                lambda x: x['price'], item['ingredients']
            )
        )
        total_price = 2 * bun_price + ingredient_price
        return total_price

    @staticmethod
    def get_ingredient_strings_from_receipt(s_arr):
        return [s for s in s_arr if re.match("=\\s(.+?)\\s=$", s)]

    @staticmethod
    def split_text_by_lines(text):
        return list(
            filter(lambda s: s != '', text.split('\n'))
        )
